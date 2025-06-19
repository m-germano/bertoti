from smolagents import CodeAgent, tool, HfApiModel, LiteLLMModel, OpenAIServerModel
from browser_use import Browser, BrowserConfig, Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import subprocess
import asyncio
import os
import time

load_dotenv()

@tool
def start_browser_session() -> str:
    """
    Inicia o navegador Google Chrome com suporte ao protocolo CDP.
    """
    chrome_path = os.getenv("CHROME_PATH")
    user_data_dir = r"C:\tmp\cdp-profile"

    try:
        subprocess.Popen([
            chrome_path,
            "--remote-debugging-port=9222",
            f"--user-data-dir={user_data_dir}"
        ])
        time.sleep(3)  # Tempo para garantir que o navegador esteja pronto
        return "Chrome iniciado com sucesso via CDP!"
    except Exception as e:
        return f"Erro ao iniciar o Chrome: {str(e)}"
    
# --- LLM para uso no browser-use (Gemini API)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", 
    api_key=os.getenv("GOOGLE_API_KEY"),
)

# --- Browser do browser-use
browser = Browser(
    config=BrowserConfig(
        cdp_url="http://localhost:9222"
    )
)

# Lista para armazenar as vagas
vagas = []

task = """
1. Acesse o site https://www.linkedin.com/.
2. Certifique-se de que o usuário está logado (perfil com login salvo deve carregar automaticamente).
3. Clique no menu "Vagas" (ícone de mala no topo da página).
4. No campo de busca, digite "Desenvolvedor Java" (ou outro termo de interesse).
5. No campo de localização, digite "São Paulo, Brasil" (ou outra cidade desejada).
6. Pressione Enter para realizar a busca.
7. Aguarde os resultados e role a página para carregar mais vagas.
8. Leia as 3 primeiras vagas exibidas e colete as seguintes informações:
   - Título da vaga
   - Nome da empresa
   - Localização
   - Há quanto tempo foi publicada
   - Link da vaga
9. Exiba essas informações como uma lista organizada.
"""

@tool
async def execute_browser_agent() -> str:
    """
    Usa o agente do browser-use para acessar o Google e procurar pela task que foi estabelecida
    """
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
    )

    # Coletando as vagas no formato de dicionário
    global vagas
    vagas = await agent.run()
    
    # Função para salvar os dados coletados em um arquivo TXT
    save_vagas(vagas)
    
    return "Tarefa no browser-use concluída com sucesso."

def save_vagas(vagas_data):
    """
    Função para salvar as vagas em um arquivo de texto (TXT).
    """
    with open("vagas_encontradas.txt", "w", encoding="utf-8") as file:
        for vaga in vagas_data:
            file.write(f"Título: {vaga['titulo']}\n")
            file.write(f"Empresa: {vaga['empresa']}\n")
            file.write(f"Localização: {vaga['localizacao']}\n")
            file.write(f"Publicado: {vaga['publicado']}\n")
            file.write("\n" + "-"*40 + "\n")  # Separador entre as vagas
    print("Vagas salvas com sucesso em vagas_encontradas.txt!")

ollamaLlm = LiteLLMModel(model_id="ollama_chat/phi4-mini", api_base='http://localhost:11434', num_ctx=8192)

model = OpenAIServerModel(
    model_id="gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    # Google Gemini OpenAI-compatible API base URL
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = CodeAgent(
    model=model,
    tools=[
        start_browser_session,
        execute_browser_agent,
    ],
    max_steps=5,
    verbosity_level=2,
    additional_authorized_imports=["asyncio", 'requests', 'bs4']
)

# --- Execução
async def main():
    result = await agent.run("Inicie o navegador e execute o browser agent")
    print(result)
    input("Pressione ENTER para fechar o navegador...")
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

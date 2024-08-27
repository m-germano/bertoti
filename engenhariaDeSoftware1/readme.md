# ENGENHARIA DE SOFTWARE I - GIULIANO ARAUJO BERTOTI

## 📝 Atividade 1 - Interpretação de texto 

### Texto 1
"We see three critical differences between programming and software engineering: time, scale, and the trade-offs at play. On a software engineering project, engineers need to be more concerned with the passage of time and the eventual need for change. In a software
engineering organization, we need to be more concerned about scale and efficiency, both for the software we produce as well as for the organization that is producing it. Finally, as software engineers, we are asked to make more complex decisions with higher-stakes
outcomes, often based on imprecise estimates of time and growth."



Comentário: Na definição acima percebemos que:  programação foca na escrita de código, enquanto engenharia de software abrange a criação e gestão de sistemas complexos, considerando tempo, escala e decisões de impacto.

### Texto 2
Within Google, we sometimes say, “Software engineering is programming integrated over time.” Programming is certainly a significant part of software engineering: after all, programming is how you generate new software in the first place. If you accept this distinction, it also becomes clear that we might need to delineate between programming tasks (development) and software engineering tasks (development, modification, maintenance). The addition of time adds an important new dimension to programming. Cubes aren’t squares, distance isn’t velocity. Software engineering isn’t programming.

Comentário: O texto discute a diferença entre "programação" e "engenharia de software". Ele sugere que a programação é apenas uma parte da engenharia de software. A programação é vista como a criação de novos softwares, enquanto a engenharia de software abrange não só a programação, mas também outras tarefas como desenvolvimento, modificação e manutenção ao longo do tempo. A ideia central é que, assim como cubos não são apenas quadrados e distância não é a mesma coisa que velocidade, a engenharia de software não é simplesmente programação. A dimensão do tempo adiciona uma camada importante à engenharia de software, diferenciando-a da programação pura.


### Duas tecnologias e comparar com requisitos não funcionais 
Linguagens de programação requisitos: nível de facilidade/usabilidade para pessoas em geral: Para interface humana em que o nível de processamento não necessita ser alto nem extremamente rápido - Python. Para interface humana em que o nível de processamento não necessita ser extremamente fácil, mas precisa estar mais próximo da linguagem de máquina - Java.

Portabilidade:
Para desenvolvimento de sistemas embarcados: Assembly, devido à sua capacidade de otimização para hardware específico e controle direto sobre os recursos de hardware.
Para desenvolvimento de aplicativos multiplataforma: Java, que é conhecida por sua portabilidade devido ao lema "escreva uma vez, execute em qualquer lugar", possibilitando a execução em diferentes plataformas através da Java Virtual Machine (JVM).

Chip de processamento: 
Para aplicações básicas: Intel Celeron J4005
Para clima: Blue Waters da NVIDIA - Supercomputador utilizado para modelagem climática no Laboratório Nacional de Urbana-Champaign.
<br>
<br>
## 📝 Atividade 2 -> 3 Exemplos de Trade-offs com requisitos não funcionais

### 1. Desempenho vs. Manutenibilidade
Exemplo: Em um sistema de alta performance, como um motor de jogo ou um aplicativo financeiro em tempo real, os desenvolvedores podem optar por usar algoritmos altamente otimizados e técnicas de programação de baixo nível para maximizar a velocidade e a eficiência. No entanto, isso pode resultar em código mais complexo e difícil de manter.

Trade-off: A escolha de priorizar desempenho pode levar a uma menor manutenibilidade do código, tornando-o mais difícil de entender e atualizar no futuro. As melhorias no desempenho podem vir à custa de uma base de código que é mais propensa a erros e mais difícil de modificar.

### 2. Segurança vs. Usabilidade
Exemplo: Em um sistema bancário, pode-se implementar medidas de segurança rigorosas, como autenticação multifatorial, criptografia de dados e monitoramento de atividades suspeitas. Embora essas medidas aumentem a segurança, podem tornar o sistema mais complexo e menos amigável para o usuário.

Trade-off: A implementação de altos níveis de segurança pode prejudicar a usabilidade do sistema, tornando-o mais difícil de usar e menos eficiente para os usuários finais. A experiência do usuário pode ser afetada por processos de autenticação mais demorados e interfaces mais complexas.

### 3. Escalabilidade vs. Custo
Exemplo: Uma empresa pode projetar uma aplicação web para escalar horizontalmente (adicionando mais servidores) para lidar com uma grande quantidade de tráfego. Isso pode envolver o uso de arquiteturas complexas, como microsserviços e balanceadores de carga, e pode exigir mais recursos e infraestrutura.

Trade-off: O aumento da escalabilidade pode levar a um aumento significativo nos custos de infraestrutura e operação. A implementação de soluções escaláveis pode exigir investimentos em hardware adicional, licenças de software e serviços de nuvem, além de custos adicionais de manutenção e suporte.

Esses trade-offs ilustram como otimizar para um requisito não funcional pode impactar outros aspectos do sistema, e como é importante equilibrar as prioridades com base nas necessidades e restrições do projeto.

## 📝 Atividade 3 -> Escolher a arquitetura de uma empresa e comentar seus tradeoffs
### Companhia escolhida: Netflix 

![WhatsApp Image 2024-08-15 at 11 56 39](https://github.com/user-attachments/assets/80e3f559-25df-4820-be6f-8f1e89601b1f)
A imagem foi obtida por meio de @alexxubyte.

### ⚖️ Primeiro Exemplo de Trade-off:  Escalabilidade vs. Complexidade Operacional:
Escalabilidade: A arquitetura de microserviços permite que a Netflix escale de forma eficiente, com cada serviço sendo independente e podendo ser escalado conforme necessário. Isso é crucial para lidar com milhões de usuários simultâneos em todo o mundo.

Complexidade Operacional: O gerenciamento de um grande número de microserviços aumenta a complexidade operacional. A Netflix precisa de uma infraestrutura robusta para monitorar, atualizar e orquestrar esses serviços, além de lidar com a comunicação entre eles.

### ⚖️ Segundo Exemplo de Trade-off: Custo vs. Disponibilidade:
Custo: A operação em nuvem e o uso intensivo de microserviços podem ser caros, especialmente em termos de custos de infraestrutura, largura de banda, e gerenciamento de dados distribuídos globalmente.

Disponibilidade: Esses custos são justificados pela alta disponibilidade que a Netflix pode oferecer aos seus usuários, garantindo que o serviço esteja disponível praticamente o tempo todo, em qualquer lugar do mundo.


## 📝 Atividade 4 -> Diagramas de classe UML e codigo exemplo
O programa abaixo, em Java, é um exemplo simples de um sistema de pedidos, envolvendo as classes Produto, Pedido, PedidoItem, e Cliente.
```java

//Cliente.java
package entities;

public class Cliente {
	private String nome;
    private String endereco;

    public Cliente(String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void fazerPedido(Pedido pedido) {
        System.out.println("Pedido feito por " + nome + " no endereço: " + endereco);
        System.out.println("Data do pedido: " + pedido.getData());
        System.out.println("Total do pedido: " + pedido.calcularTotal());
    }
}

// Pedido.java
package entities;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Pedido {
	private Cliente cliente;
    private List<PedidoItem> itens;
    private Date data;

    public Pedido(Cliente cliente) {
        this.cliente = cliente;
        this.itens = new ArrayList<>();
        this.data = new Date();
    }

    public void adicionarItem(PedidoItem item) {
        itens.add(item);
    }

    public double calcularTotal() {
        double total = 0.0;
        for (PedidoItem item : itens) {
            total += item.calcularPrecoTotal();
        }
        return total;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public List<PedidoItem> getItens() {
        return itens;
    }

    public Date getData() {
        return data;
    }
}

//PedidoItem.java


package entities;

public class PedidoItem {
	private Produto produto;
    private int quantidade;

    public PedidoItem(Produto produto, int quantidade) {
        this.produto = produto;
        this.quantidade = quantidade;
    }

    public double calcularPrecoTotal() {
        return produto.getPreco() * quantidade;
    }

    public Produto getProduto() {
        return produto;
    }

    public int getQuantidade() {
        return quantidade;
    }
}

//Produto.java

package entities;

public class Produto {
	private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }
}

```
![Diagrama em branco (1)](https://github.com/user-attachments/assets/1a8437f0-afe1-471f-a54b-df964673badc)


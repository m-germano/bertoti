
# Strategy Pattern

O **Strategy Pattern** é um padrão de projeto comportamental que define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Isso permite alterar o comportamento de um objeto em tempo de execução sem modificar sua estrutura.

## Quando usar?

- Quando existem múltiplas variações de um algoritmo (ex.: cálculo de desconto, formas de pagamento, cálculo de frete).  
- Para evitar condicionais complexas (if/switch) ao selecionar o algoritmo.  
- Para seguir o princípio **Open/Closed**: aberto para extensão, fechado para modificação.

## Estrutura do padrão

- **Interface Strategy**: define o método que todas as estratégias devem implementar.  
- **Concrete Strategies**: implementam diferentes algoritmos.  
- **Context**: utiliza a Strategy e pode alterar sua implementação dinamicamente.

## Exemplo em Java

```java
interface FreteStrategy {
    double calcular(double peso);
}

class Sedex implements FreteStrategy {
    @Override
    public double calcular(double peso) {
        return peso * 10; 
    }
}

class PAC implements FreteStrategy {
    @Override
    public double calcular(double peso) {
        return peso * 5;
    }
}

class CalculadoraFrete {
    private FreteStrategy strategy;

    public CalculadoraFrete(FreteStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(FreteStrategy strategy) {
        this.strategy = strategy;
    }

    public double calcularFrete(double peso) {
        return strategy.calcular(peso);
    }
}

public class Main {
    public static void main(String[] args) {
        CalculadoraFrete calculadora = new CalculadoraFrete(new Sedex());
        System.out.println("Sedex: R$" + calculadora.calcularFrete(2)); 

        calculadora.setStrategy(new PAC());
        System.out.println("PAC: R$" + calculadora.calcularFrete(2));
    }
}
```

## Vantagens

- Facilita a manutenção e extensão do código.  
- Evita duplicação e grandes blocos de condicionais.  
- Permite trocar algoritmos em tempo de execução.

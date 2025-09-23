
# Anti-Pattern: Strategy Implementado com Herança

O anti-pattern de **Strategy via herança** ocorre quando, ao invés de usar composição para definir comportamentos intercambiáveis, tentamos resolver tudo estendendo classes. Isso leva a um código rígido e difícil de manter.

## Por que isso é problemático?

- **Árvore de herança inflexível**: Cada nova variação requer uma nova subclasse.  
- **Manutenção complicada**: Com múltiplas combinações de comportamento, a quantidade de classes cresce rapidamente.  
- **Violação do Princípio Open/Closed**: Para introduzir uma nova estratégia, você precisa alterar classes existentes.  
- **Troca dinâmica impossível**: Não dá para mudar o comportamento em tempo de execução; é preciso instanciar outra classe.

## Exemplo Prático: Cálculo de Frete com Herança (Anti-Pattern)

```java
class CalculadoraFrete {
    public double calcular(double peso) {
        return peso * 10;
    }
}

class CalculadoraFretePAC extends CalculadoraFrete {
    @Override
    public double calcular(double peso) {
        return peso * 5;
    }
}

class CalculadoraFreteTransportadora extends CalculadoraFrete {
    @Override
    public double calcular(double peso) {
        return peso * 8;
    }
}

public class MainAntiPattern {
    public static void main(String[] args) {
        CalculadoraFrete sedex = new CalculadoraFrete();
        System.out.println("Sedex: R$" + sedex.calcular(2));

        CalculadoraFrete pac = new CalculadoraFretePAC();
        System.out.println("PAC: R$" + pac.calcular(2));

        CalculadoraFrete transportadora = new CalculadoraFreteTransportadora();
        System.out.println("Transportadora: R$" + transportadora.calcular(2));
    }
}
```

## Por que evitar este padrão

- Cada nova regra de frete exige criar uma nova subclasse.  
- Mudanças nos cálculos existentes podem afetar várias classes.  
- Não é possível trocar o tipo de frete em tempo de execução sem criar um novo objeto.  

**Conclusão:** usar herança para implementar Strategy limita flexibilidade e escalabilidade. O ideal é adotar **composição**, injetando comportamentos dinamicamente via interfaces ou classes funcionais.

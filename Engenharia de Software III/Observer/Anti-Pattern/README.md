# Observer Anti-Pattern - Exemplo em Java

Este exemplo mostra um anti-pattern: o Subject conhece detalhes das classes concretas e usa `instanceof` para chamar métodos diferentes.  
Isso viola o princípio do aberto/fechado (OCP) e gera forte acoplamento.

## Código

```java
// AntiSubject.java
import java.util.ArrayList;
import java.util.List;

public class AntiSubject {
    private final List<Object> observers = new ArrayList<>();
    private String state;

    public void add(Object o) {
        observers.add(o);
    }

    public void remove(Object o) {
        observers.remove(o);
    }

    // Anti-pattern: usa instanceof e casting
    public void notifyAllWrong() {
        for (Object o : observers) {
            if (o instanceof ConcreteObserverA) {
                ((ConcreteObserverA) o).receiveA(state);
            } else if (o instanceof ConcreteObserverB) {
                ((ConcreteObserverB) o).receiveB(state);
            }
        }
    }

    public void setState(String newState) {
        this.state = newState;
        notifyAllWrong();
    }
}

// ConcreteObserverA.java
public class ConcreteObserverA {
    private final String id;
    public ConcreteObserverA(String id) { this.id = id; }
    public void receiveA(String state) {
        System.out.println("A[" + id + "] recebeu: " + state);
    }
}

// ConcreteObserverB.java
public class ConcreteObserverB {
    private final String id;
    public ConcreteObserverB(String id) { this.id = id; }
    public void receiveB(String state) {
        System.out.println("B[" + id + "] recebeu: " + state);
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        AntiSubject subject = new AntiSubject();
        ConcreteObserverA a = new ConcreteObserverA("1");
        ConcreteObserverB b = new ConcreteObserverB("X");

        subject.add(a);
        subject.add(b);

        subject.setState("estado 1");
    }
}
```

## Problemas
- Forte acoplamento.  
- Mudança no Subject sempre que um novo Observer é criado.  
- Baixa flexibilidade e reutilização.  

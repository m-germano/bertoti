# Observer Pattern - Exemplo em Java

O Observer é usado para desacoplar a fonte de eventos (Subject) dos seus consumidores (Observers).  
Cada Observer se registra no Subject, e este notifica todos quando seu estado muda.

## Código

```java
// Subject.java
public interface Subject {
    void registerObserver(Observer o);
    void removeObserver(Observer o);
    void notifyObservers();
}

// Observer.java
public interface Observer {
    void update(String state);
}

// ConcreteSubject.java
import java.util.ArrayList;
import java.util.List;

public class ConcreteSubject implements Subject {
    private final List<Observer> observers = new ArrayList<>();
    private String state;

    @Override
    public void registerObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for (Observer o : observers) {
            o.update(state);
        }
    }

    public void setState(String newState) {
        this.state = newState;
        notifyObservers();
    }
}

// ConcreteObserver.java
public class ConcreteObserver implements Observer {
    private final String name;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    @Override
    public void update(String state) {
        System.out.println("Observer " + name + " recebeu atualização: " + state);
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        ConcreteSubject subject = new ConcreteSubject();
        ConcreteObserver o1 = new ConcreteObserver("A");
        ConcreteObserver o2 = new ConcreteObserver("B");

        subject.registerObserver(o1);
        subject.registerObserver(o2);

        subject.setState("estado 1");
        subject.removeObserver(o1);
        subject.setState("estado 2");
    }
}
```

## Vantagens
- Desacoplamento entre Subject e Observers.  
- Fácil extensão, basta criar novos Observers sem mudar o Subject.  

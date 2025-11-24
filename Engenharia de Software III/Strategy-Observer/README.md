# Exemplo Observer + Strategy (Sensor de Movimento + Estratégias de Alerta)

Este exemplo combina Observer e Strategy em um sistema simples de detecção de movimento.  
Quando o sensor detecta algo, ele notifica observadores.  
Cada observador usa uma estratégia diferente para reagir ao evento.

## Estrutura

- **Observer**: recebe eventos (Alarm, Logger).
- **Subject**: sensor que dispara notificações (MotionSensor).
- **Strategy**: define como lidar com o alerta (BeepStrategy, SilentLogStrategy, SmsStrategy, etc).

---

## Código

```java
import java.util.ArrayList;
import java.util.List;

// OBSERVER
interface Observer {
    void update(String event);
}

// SUBJECT
class MotionSensor {
    private final List<Observer> observers = new ArrayList<>();

    public void subscribe(Observer o) {
        observers.add(o);
    }

    public void unsubscribe(Observer o) {
        observers.remove(o);
    }

    public void detectMovement() {
        notifyAll("Movimento detectado!");
    }

    private void notifyAll(String event) {
        for (Observer o : observers) {
            o.update(event);
        }
    }
}

// STRATEGY
interface AlertStrategy {
    void alert(String message);
}

// Estratégias específicas
class BeepStrategy implements AlertStrategy {
    @Override
    public void alert(String message) {
        System.out.println("BEEP! " + message);
    }
}

class SmsStrategy implements AlertStrategy {
    @Override
    public void alert(String message) {
        System.out.println("Enviando SMS: " + message);
    }
}

class SilentLogStrategy implements AlertStrategy {
    @Override
    public void alert(String message) {
        System.out.println("(Log silencioso) -> " + message);
    }
}

// Observers usando Strategy
class AlarmObserver implements Observer {
    private AlertStrategy strategy;

    AlarmObserver(AlertStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(AlertStrategy strategy) {
        this.strategy = strategy;
    }

    @Override
    public void update(String event) {
        strategy.alert(event);
    }
}

class LoggingObserver implements Observer {
    private AlertStrategy strategy;

    LoggingObserver(AlertStrategy strategy) {
        this.strategy = strategy;
    }

    @Override
    public void update(String event) {
        strategy.alert("Registro: " + event);
    }
}

// MAIN
public class StrategyObserverDemo {
    public static void main(String[] args) {
        MotionSensor sensor = new MotionSensor();

        AlarmObserver alarm = new AlarmObserver(new BeepStrategy());
        LoggingObserver logger = new LoggingObserver(new SilentLogStrategy());

        sensor.subscribe(alarm);
        sensor.subscribe(logger);

        sensor.detectMovement();

        alarm.setStrategy(new SmsStrategy());

        sensor.detectMovement();
    }
}

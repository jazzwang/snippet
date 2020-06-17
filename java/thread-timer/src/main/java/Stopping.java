import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by jazz on 2017/06/05.
 *
 * Ref: https://www.tutorialspoint.com/javaexamples/thread_stop.htm
 */
public class Stopping {
    public static void main(String[] args) {
        final CanStop stoppable = new CanStop();
        stoppable.start();

        new Timer(true).schedule(new TimerTask() {
                                     public void run() {
                                         System.out.println("Requesting stop");
                                         stoppable.requestStop();
                                     }
                                 },
                350);
    }
}

class CanStop extends Thread {
    private volatile boolean stop = false;
    private int counter = 0;

    public void run() {
        while (!stop && counter < 10000) {
            try {
                sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(counter++);
        }
        if (stop)
            System.out.println("Detected stop");
    }
    public void requestStop() {
        stop = true;
    }
}
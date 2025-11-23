import java.util.ArrayList;
import java.util.List;


/**
 * Small playground that wires a producer and consumer together over a homemade blocking queue.
 * The goal is to show the flow of data rather than hide everything behind library calls.
 */
public class ProducerConsumerExample {

    /**
     * Simulates data transfer:
     * source list -> blocking queue -> destination list.
     */
    public static List<Integer> transfer(List<Integer> source) throws InterruptedException {
        BlockingQueue<Integer> queue = new BlockingQueue<>(5);

        List<Integer> destination = new ArrayList<>();
        Producer producer = new Producer(queue, source);
        Consumer consumer = new Consumer(queue, destination, source.size());

        // Spin up the two workers so they can run at their own pace.
        Thread producerThread = new Thread(producer, "producer-thread");
        Thread consumerThread = new Thread(consumer, "consumer-thread");

        producerThread.start();
        consumerThread.start();

        // Wait for both threads so we only return after all work is done.
        producerThread.join();
        consumerThread.join();

        return destination;
    }

    // Optional manual demo
    public static void main(String[] args) throws InterruptedException {
        List<Integer> source = List.of(1, 2, 3, 4, 5);
        List<Integer> result = transfer(source);
        System.out.println("Destination container: " + result);
    }
}

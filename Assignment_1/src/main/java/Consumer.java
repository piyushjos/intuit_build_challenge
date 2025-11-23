import java.util.List;

/**
 * Consumer takes items from the queue and stores them in destination.
 * Picture someone steadily grabbing snacks off the table.
 */
public class Consumer implements Runnable {

    private final BlockingQueue<Integer> queue;
    private final List<Integer> destination;
    private final int itemsToConsume;

    public Consumer(BlockingQueue<Integer> queue,
                    List<Integer> destination,
                    int itemsToConsume) {
        this.queue = queue;
        this.destination = destination;
        this.itemsToConsume = itemsToConsume;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < itemsToConsume; i++) {
                Integer value = queue.take();
                // Keep the destination list in the same order items were taken.
                destination.add(value);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

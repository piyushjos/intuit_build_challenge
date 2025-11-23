import java.util.LinkedList;
import java.util.Queue;

/**
 * Tiny, hand-rolled blocking queue to keep the producer/consumer example easy to read.
 * It uses the classic wait/notify pattern instead of leaning on java.util.concurrent.
 */
public class BlockingQueue<T> {
    // Items sit in this in-memory queue until a consumer takes them.
    private final Queue<T> queue = new LinkedList<>();
    // Hard cap so producers back off instead of piling up.
    private final int capacity;

    public BlockingQueue(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("Capacity must be > 0");
        }
        this.capacity = capacity;
    }

    /**
     * Adds an item to the queue. If the queue is full, wait politely for space.
     */
    public synchronized void AddItem(T item) throws InterruptedException {
        while (queue.size() == capacity) {
            // Another thread will notify us when an item is removed.
            wait();
        }
        queue.add(item);
        // Wake up waiting consumers so they can grab the new item.
        notifyAll();
    }

    /**
     * Takes an item from the queue. If empty, wait until a producer brings something.
     */
    public synchronized T take() throws InterruptedException {
        while (queue.isEmpty()) {
            // Sleep until a producer drops off a new item.
            wait();
        }
        T item = queue.remove();
        // Wake producers in case they were blocked by capacity.
        notifyAll();
        return item;
    }
}

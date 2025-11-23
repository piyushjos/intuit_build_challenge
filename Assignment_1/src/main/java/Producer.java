import java.util.List;

/**
 * Producer reads numbers from a source list and hands them to the shared queue.
 * Think of it as the friend dropping snacks on the table.
 */
public class Producer implements Runnable {

    private final BlockingQueue<Integer> queue;
    private final List<Integer> source;

    public Producer(BlockingQueue<Integer> queue, List<Integer> source) {
        this.queue = queue;
        this.source = source;
    }

    @Override
    public void run() {
        try {
            for (Integer value : source) {
                // Push each value into the queue; may block if the queue is at capacity.
                queue.AddItem(value);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

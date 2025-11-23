import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class ProducerConsumerExampleTest {

    @Test
    void testAllItemorder() throws InterruptedException {
        List<Integer> source = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        List<Integer> destination = ProducerConsumerExample.transfer(source);

        // Every item should make the trip, staying in order.
        assertEquals(source.size(), destination.size());
        assertEquals(source, destination);
    }

    @Test
    void checkhEmptySource() throws InterruptedException {
        List<Integer> source = List.of();

        List<Integer> destination = ProducerConsumerExample.transfer(source);

        // With nothing to produce, we expect nothing to consume.
        assertTrue(destination.isEmpty());
    }

    @Test
    void testforSingleElement() throws InterruptedException {
        List<Integer> source = List.of(42);

        List<Integer> destination = ProducerConsumerExample.transfer(source);

        // Single value should pass straight through untouched.
        assertEquals(1, destination.size());
        assertEquals(42, destination.get(0));
    }
}

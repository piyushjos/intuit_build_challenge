# Assignment 1 - Producer/Consumer Demo

Small Java 21 Maven project that demonstrates the producer-consumer pattern using a hand-rolled blocking queue. This section covers Assignment 1

## Code tour
- `src/main/java/BlockingQueue.java` - minimal synchronized queue built with wait/notify and a fixed capacity.
- `src/main/java/Producer.java` - reads integers from a source list and enqueues them, blocking when the queue is full.
- `src/main/java/Consumer.java` - dequeues integers, preserves order, and stores them in a destination list.
- `src/main/java/ProducerConsumerExample.java` - wires producer and consumer threads via `transfer`; includes an optional `main` demo.
- `src/test/java/ProducerConsumerExampleTest.java` - JUnit tests that validate ordering, empties, and single-item cases.

## Prerequisites
- Java 21
- Maven 3.9+ (or compatible)

## Setup and run
1) Clone/download the project and open it in your IDE or terminal.  
2) Ensure `JAVA_HOME` points to Java 21 and `mvn -v` works.  
3) Run tests: `mvn test`  
4) Build only: `mvn -q -DskipTests compile`  
5) Run the demo after compiling: `java -cp target/classes ProducerConsumerExample`

## Build and test
- Run the test suite: `mvn test`
- Compile the project: `mvn -q -DskipTests compile`
- Run the demo manually after compiling: `java -cp target/classes ProducerConsumerExample`

## How it works
- The producer iterates through a provided `List<Integer>`, blocking when the queue reaches capacity.
- The consumer takes the same number of items, blocking when the queue is empty so it never misses data.
- `transfer` coordinates both threads, waits for them to finish, and returns the filled destination list.

## Sample output
Running `java -cp target/classes ProducerConsumerExample` prints:
```text
Destination container: [1, 2, 3, 4, 5]
```


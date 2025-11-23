# Intuit Build Challenge – Assignments 1 & 2

This repository contains the completed solutions for the **Intuit Build Challenge**, covering:

* Java multithreading (Producer–Consumer)
* Python functional programming (CSV Data Analysis)
* Unit testing
* Clean project structure and documentation

Each assignment is placed in its own folder with full source code, tests, and its own README.

---

## Badges

![Java](https://img.shields.io/badge/Language-Java-blue?logo=java\&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python\&logoColor=white)
![Maven](https://img.shields.io/badge/Build-Maven-red?logo=apachemaven\&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Assignment 1 – Producer–Consumer Pattern (Java)

**Goal:**
Implement a classic *Producer–Consumer* pattern demonstrating:

* Custom blocking queue
* Thread synchronization
* `wait()` and `notifyAll()`
* Producer and Consumer threads
* JUnit tests

**Technologies Used:**

* Java
* Multithreading
* Maven
* JUnit 5

**Folder:**
👉 [Assignment_1](Assignment_1)

Inside the folder:

* `BlockingQueue.java`
* `Producer.java`
* `Consumer.java`
* `ProducerConsumerExample.java`
* JUnit test suite
* README with setup instructions

---

# Assignment 2 – Sales Data Analysis (Python)

**Goal:**
Perform CSV sales data analysis using functional programming techniques such as:

* Lambda expressions
* Iterator/stream-style grouping
* Aggregations by product line, region, and month
* Top-N revenue categories
* Real sales dataset
* Unit tests

**Dataset:**

* Uses `sales_data_sample.csv`
* `PRODUCTLINE` used as product category
* `COUNTRY` used as region

**Technologies Used:**

* Python
* Functional programming
* `csv`, `itertools.groupby`
* Python `unittest`

**Folder:**
👉 [Assignment_2](Assignment_2)

Inside the folder:

* `analysis.py`
* `main.py`
* `tests/`
* `data/sales_data_sample.csv`
* README with explanation and sample output

---

# Repository Structure

```
intuit_build_challenge/
├── Assignment_1/
│   ├── src/
│   ├── pom.xml
│   └── README.md
├── Assignment_2/
│   ├── analysis.py
│   ├── main.py
│   ├── data/
│   │   └── sales_data_sample.csv
│   ├── tests/
│   └── README.md
├── .gitignore
└── README.md
```

---

# How to Run

### Assignment 1 (Java)

```
cd Assignment_1
mvn clean install
mvn test
```

Run the program using IntelliJ or:

```
mvn exec:java -Dexec.mainClass=ProducerConsumerExample
```

---

### Assignment 2 (Python)

```
cd Assignment_2
python main.py
```

Run tests:

```
python -m unittest discover -s tests
```

---

# Skills Demonstrated

### Assignment 1

* Java concurrency
* Synchronization and thread coordination
* Custom blocking queue design
* JUnit testing

### Assignment 2

* Functional programming patterns
* Data transformations and grouping
* Real-world CSV analysis
* Python unittest framework

---

# Notes

Refer to each assignment’s folder for detailed implementation walkthrough, assumptions, and sample output.

---


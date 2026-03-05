# Student Data Management System Lab

## Learning Goals

- Utilize **lists, tuples, and sets** to store and manage student records.
- Apply **list comprehensions** and **dictionary comprehensions** for efficient data filtering.
- Use **generator expressions** to process large datasets efficiently.
- Implement **set operations** for tracking unique student attributes.
- Structure a Python application with modular data management techniques.

## Introduction

In this lab, you will build a **Student Data Management System** that allows users to store, filter, and process student records efficiently. The system will enable users to:

- Store and retrieve student information using **lists, tuples, and sets**.
- Filter student data dynamically using **list comprehensions** and **dictionary comprehensions**.
- Process large student datasets efficiently using **generator expressions**.
- Track unique student attributes (e.g., **majors, completed courses**) using **sets**.

This lab will help you apply Python **data structures** to solve real-world problems efficiently and dynamically.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine using:
   ```sh
   git clone <repo-url>
   cd course-7-module-1-python-data-structures-lab
   ```

### Install Dependencies

Ensure **Python** is installed:
```sh
python --version
```

Run the following command to install dependencies:
```sh
pipenv install
```

Run the following to enter the virtual environment:
```sh
pipenv shell
```

To run the test suite, use:
```sh
pytest -x
```

## Tasks

### Task 1: Define the Problem

The goal of this lab is to build a **Student Data Management System** that allows users to store, retrieve, and process student records efficiently. The system must provide the following capabilities:

- Manage student records using **lists, tuples, and sets**.
- Filter student data dynamically using **list comprehensions** and **set comprehensions**.
- Process large datasets efficiently using **generator expressions**.
- Track unique student attributes (e.g., completed courses) using **sets**.

The key challenge is to apply **efficient Python data structures** to dynamically handle, filter, and process student information.

---

### Task 2: Determine the Design

The **Student Data Management System** will be built using structured data handling techniques, including:

- **Lists & Tuples**: Store student data in structured collections.
- **List Comprehensions & Generator Expressions**: Process and filter student records efficiently.
- **Sets**: Track unique student data attributes such as completed courses and enrolled majors.

#### Design Breakdown:
- **Student list storage** using **tuples** and **lists**.
- **Filtering capabilities** using **list comprehensions**.
- **Memory-efficient data handling** with **generator expressions**.
- **Tracking unique attributes** using **sets**.

This structured approach ensures an **efficient, maintainable, and scalable** student data system.

---

### Task 3: Develop the Code

#### Step 1: Define Student Records using Lists and Tuples

In `student_data.py`, define a list of students as tuples. You can use the example below,
or make up your own student data.

```python
# List of students stored as tuples (ID, Name, Major)
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]
```

#### Step 2: Filtering Students Using List Comprehensions

In `filter.py`, edit the `filter_students_by_major` function to return a filtered list
of students given a major using a list comprehension.

#### Step 3: Displaying Student Data

In `data_processing.py`, edit the `format_student_data` function to return a string for a given student formatted like:
```python
"ID: 10 | Name: Louis Medina | Major: Computer Science"
```

#### Step 4: Displaying All Students' Data

In `data_processing.py`, edit the `display_students` function to loop through all students and print each student's
details using the `format_student_data` function.

#### Step 5: Updating Student Courses Using Set Operations

In `set_operations.py`, edit the `unique_majors` function to return a set of unique student
majors using set comprehension. For example, given a list of students like:
```python
[
    (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]
```
the `unique_majors` function should return (in no particular order):
```python
{"Mathematics", "Physics"}
```

#### Step 6: Create a Student List Generator by Major

In `data_generator.py`, edit the `student_generator` function to return a generator expression
for all students by major. Example of a generator expression:

```python
(item_to_return for item_in_iterable in iterable if condition)

# more concrete example:
number_list = [1,2,3,4,5,6]
generator_expression = (n * 2 for n in number_list if n > 3)
```


---

## Best Practices for Managing Student Data

- **Use comments** to clarify logic.
- **Optimize lookups** with dictionary `.get()` method.
- **Use set operations** for efficient course tracking.
- **Apply generator expressions** for memory efficiency.
- **Update README** to document functionality.

## Conclusion

By mastering **Sequences, List Comprehensions, Generator Expressions, Dictionaries, and Sets**, developers can:

- Optimize **student data storage and retrieval**.
- Enhance **performance using efficient data structures**.
- Improve **scalability using structured data management techniques**.

This lab ensures real-world applicability of Python **data structures** in managing dynamic, scalable, and efficient datasets.
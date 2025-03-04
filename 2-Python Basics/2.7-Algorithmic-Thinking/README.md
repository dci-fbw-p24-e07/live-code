# Algorithmic Thinking

## 04.03.25 - Intro to Algorithmic Thinking

- What is an Algorithm?
- What is Algorithmic Thinking?
- Types of Algorithms in programming
- Typical/Common algorithms in programming
- What is Pseudo Code?
- How to write Pseudo Code

### What is an algorithm?

- An algorithm is a set of defined steps used to perform a specific objective. 
- This can be a simple process like baking a cake, or a complex series of operations as used in machine learning to analyze data and make predictions

- Typical steps/structure found in an algorithm:

1. **Input:** Defining inputs to be used in the algorithm. Can be anything from a simple value to a complex data structure.

2. **Processing:** This is where the algorithm performs operations on the inputs using a series of computational steps. This phase is guided by logical and arithmetic calculations. It often involves 2 crucial substeps:

    1. **Decision making:** At various points during processing decisions need to be made based on certain conditions. This involves directing the flow of the algorithm based on conditional statements.
    2. **Looping:** For many algorithms, certain steps need to be repeated multiple times until a specific condition is met.

3. **Output:** After processing the inputs through various computational and conditional steps, the algorithm produces an output. This output is the result of the algorithm's operations and is used to solve the problem of perform the task at hand.

4. **Termination:** An algorithm must have a defined stopping point to ensure it doesn't run indefinitely. Once the steps are executed successfully, and the output is produced, the algorithm reaches its termination point.

### What is Algorithmic Thinking?

- The process of thinking through a problem to determine clear/structured steps to meet the objective.
- Determining what the outcomes would be if te process is followed precisely(step-by-step)

### Types of Algorithms in Programming

1. **Sorting algorithms:** 

    - They arrange data in a particular order, typically numerical or lexicographical(alphabetic order). Which is important for optimizing other algorithms that may require sorted data to function correctly.
    - Sorted data structures facilitate quicker data retrieval and are essential in database indexing.

    **Examples:**

    1. *Quick Sort:* Utilizes the divide-and-conquer approach to partition arrays and sort th elements efficiently.
    2. *Merge Sort:* Also a divide-and-conquer algorithm that divides the array into halves and then merges the sorted halves.
    3. *Bubble Sort:* Compares the two adjacent elements and swaps them until they are in the intended order.

2. **Search Algorithms:**

    - They are necessary in scenarios where quick data retrieval is necessary.
    - They reduce time complexity from linear to logarithmic  significantly speeding up the data retrieval process

    **Examples:*
    1. *Linear Search:* Sequentially checks each element until the desired value is found or the list ends.
    2. *Binary Search:* Efficiently searches a **sorted** array by multiplying the search interval. 

3. Hashing Algorithms
4. Graph Algorithms
5. Recursive Algorithms
6. Machine Learning Algorithms

### Pseudocode

#### What is Pseudocode?

- A technique used to describe the distinct steps of an algorithm in a way that's easy for anyone with basic programming knowledge to follow and understand.
- The idea is to write the steps in a format that is close or identical to the desired programming language.
- It must provide a full description of the algorithms logic so that moving from pseudocode to implementation is merely a task of translating each line into code using the syntax of the given programming language.

#### Writing Pseudocode

**The Main Constructs of Pseudocode:**

- Also known as keywords

1. **SEQUENCE** represents linear tasks sequentially performed one after the other.
2. **WHILE** is a loop with a condition at the beginning
3. **REPEAT-UNTIL** is a loop with a condition at the bottom
4. **FOR** is another way of looping usually over some sort of sequence.
5. **IF-THEN-ELSE** a conditional statement changing the flow of the program

![Pseudocode Constructs](https://builtin.com/sites/www.builtin.com/files/styles/ckeditor_optimize/public/inline-images/national/pseudocode%2520constructs.png)

**Pseudocode Rules:**

1. ALWAYS capitalize the initial word (usually one of the constructs)
2. Make only one statement per line
3. Indent to show hierarchy, improve readability and show nested constructs.
4. Always end multiline sections using any of the `END` keywords(ENDIF, ENDWHILE, etc)
5. Keep your statements programming language independent
6. Use the the naming domain of the problem and not that of implementation. For example "Append the last name to the first name" instead of "name = first + last" (Use human language not computer language)
7. Keep it simple, concise and readable

**Example:**

- Say an employer is designing a 10-question, multiple choice quiz for employees to take after reading content on workplace safety. Those who get at least eight questions correct pass the quiz and receive a certificate of completion. Those who don't reach this benchmark must retake the quiz.
The psuedocode for determining those who pass and fail could look like this

```
IF employee gets eight or more questions correct
    DISPLAY message: "Congratulations you have passed"
    Transition to a printable certificate of completion page
ELSE
    DISPLAY message: "Let's try again"
    Transition back to the first page of the quiz
```

- You want to design a program to help you determine a users origins according to their name. If a user has more than 3 vowels in their name they are from a far away land. and if a user has less than 3 vowels in their name they are a local. The program should tell user their origins

```
OBTAIN the current users name
INITIALIZE the vowel count
FOR all the letter in the name
    IF the letter is a vowel
        INCREMENT the vowel count
    ENDIF
ENDFOR
IF the vowel count is more than 3
    DISPLAY message: "You are from a far away land"
ELSE
    DISPLAY message: "You are a local"
ENDIF
```

- You want to design a program that calculates the area of a triangle. The user will give you the values for the base(B) and height(H). The formula to calculate the area of a triangle is `1/2 x B x H`. Give the user the resulting area of the triangle.

```

```

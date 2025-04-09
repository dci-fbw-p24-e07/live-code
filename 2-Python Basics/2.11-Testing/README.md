# Testing

## 09.04.25 - Introduction to Testing and Test Driven Development

- What is testing?
- What is Manual Testing?
- How does Manual Testing affect software quality
- What is automated testing?
- Types of Automated Tests
- What is Test Driven Development?
- What are the phases of TDD?
- Example of Test Driven Development

### What is testing?

- Software testing is the process of evaluating and verifying that a software product or application does what it’s supposed to do. 
- The benefits of good testing include preventing bugs and improving performance.

### Manual Testing

- A testing process performed manually without automation tools, where testers validate software functionality by executing test cases step-by-step.
- Manual testing is the "default" kind of testing. Opening up a website and simply clicking on a button to see if it works already counts as manual testing.
- Manual testing is a testing approach where testers manually interact with software/app to check its quality without the help of automated testing tools or test scripts. 
- Manual testers interact with the system like how an end user would to identify bugs in the software that can create friction in the user experience. 
- For large-scale testing project where there are thousands and millions of items and features to test, QA teams usually automate their work to boost efficiency. However, manual testing is still needed for scenarios where it's impossible to automate.

**Types of Manual Testing:**
Any type of testing can be executed both manually and with the help of an automation tool. The final decision to choose which approach lies in the nature of that specific test case.

1. *Exploratory testing:* testers explore the application or software freely, without a plan, to see if they can "discover" any bugs in the process.
2. *Ad-hoc testing:* testers perform a targeted test on a certain feature because they suspect that there might be some issues there.
3. *Usability testing:* testers check if the application is usable. "Usability" is an elusive and hard-to-define term, so manual testing is a much better fit compared to the rigid and hard-coded nature of automation testing.

**Challenges Of Manual Testing:**

1. Time-Consuming
    - Manual testing requires testers to execute each and every step manually. It is fine for small projects, but for those with hundreds to thousands of test cases, manual testing is just counter-productive.
    - Moreover, humans cannot process data as fast as machines, and we are prone to fatigue and distraction. If a mistake occurs, testers must repeat steps, further extending the testing time.

2. *Limited Test Reusability*
    - Each manual test execution is independent. A new execution requires testers to repeat all steps from the beginning. This leads to:
        - Inconsistent Results – Different testers may follow slightly different approaches, leading to variations in test outcomes.
        - Scalability Issues – As test cases increase, more testers are needed, making it inefficient for large-scale projects. Automation, in contrast, allows test scripts to be reused across multiple runs.

3. *Hidden Costs*
    - While manual testing does not require specialized tools or scripting, the long-term cost can be high due to the need for more testers, longer testing cycles, and repeated effort for the same test cases. Companies often underestimate these costs when scaling their testing process.

4. *Delays in Bug Identification and Resolution*
    - Manual testing takes longer to identify and report defects. Since execution is slower, bugs may be discovered late in the development cycle, increasing the effort required for debugging and fixing them. This delay can impact release schedules and software quality.

### Automated Testing

- Automated testing is a software testing technique that automates the process of validating the functionality of software and ensures it meets requirements before being released into production.
- With automated testing, an organization can run specific software tests at a faster pace without human testers. 
- It is best suited for large or repetitive test cases.
- Automated software testing uses scripted sequences executed by testing tools.
- The tools examine the software, report outcomes and compare results with earlier test runs.
- An automated test script can be created once and then used repeatedly
- Automated tests can run repeatedly at any time of day and are an extremely important part of continuous testing, continuous integration (CI) and continuous delivery (CD) software development practices.

**Types of Automation Testing:**

- Automation testing can be particularly beneficial for repetitive tasks, ensuring consistent and reliable results. There are a wide range of types of tests that you can (and should) automate. The following list should help you decide.

1. *Unit Testing*
    - These tests are created and run by developers to ensure each function in your application is working correctly. They are easy to automate and should be run automatically whenever new code is pushed to your master branch.

2. *Integration testing*
    - Integration tests check whether modules/subunits of your application are working. These can often be tested automatically. You also need to ensure that you test both expected and unexpected inputs.

3. *System testing*
    - Once you have a complete application, you need to test the complete system. There are several types of system testing you can automate.

        1. **Functional testing**. This is where you verify that your system functions in the expected manner. For instance, when a user logs in, does the system correctly load their account details.

        2. **Regression Testing**. These are used to verify that new code hasn’t broken your existing application. They also allow you to check whether any old bugs have reappeared.

        3. **Smoke Testing**. A smoke test is a quick set of tests that verify the core functionality of your application. It’s great to automate these. That way, you can instantly test whether any new code or change to your backend has major problems.

4. *User Acceptance testing*
    - The “final” level of testing for any application is acceptance testing. This checks that the application does what the user wants it to. Some forms of acceptance testing can’t be automated, but others can be.

        1. **Performance tests**. These make sure that your backend will be able to perform under the expected load from your users. This includes stress tests, load tests, and responsiveness tests. Each of these checks a different aspect of your backend.

        2. **A/B testing**. This allows you to choose which version of a feature or UI element your users prefer or whether a new feature is popular. It can be automated relatively simply by using feature flags to turn features on and off. This is then coupled with instrumentation and analysis to understand how your users engage with the application.

5. *End to End Testing*
    - End-to-end testing evaluates a software product's entire workflow from the user's perspective, verifying the integration of all components.
    - Automating these tests can be challenging due to their complexity, but modern, capable test automation tools can facilitate this process. 
    - An ideal test automation platform for efficient end-to-end testing should be robust against fragile tests, offer automatic test maintenance, enable straightforward test creation, and provide detailed, specific data

### Manual vs Automated Testing

|  Criteria | Manual Testing | Automated Testing |
|-----------|----------------|-------------------|
| Speed | Slow, requires manual effort and execution of test cases | Faster, allows for simultaneous execution of test cases using automation tools |
| Reliability| More prone to human error | Less prone to human error, as test cases are executed using automation tools and can be repeated consistently |
| Maintenance | Requires more effort to maintain large test suites | Requires more effort to set up initially, but requires minimal effort to maintain once automation scripts are created | 
| Reusability | Tests can be reused, but require manual execution, limiting the scalability of testing | Tests can be reused multiple times with minimal effort, enabling more comprehensive and scalable testing |
| Scope | Limited in scope, requires manual effort and time, making it difficult to achieve full test coverage | Can cover a wider scope of testing, including regression testing, making it easier to achieve full test coverage |
| Cost | Lower upfront cost as it does not require specialized tools or technology, but can become more expensive over time due to increased labor costs | Higher upfront cost as it requires specialized tools and technology, but can become more cost-effective over time due to increased efficiency |
| Skillset | Requires a tester with manual testing skills, including an understanding of the application being tested and the ability to identify and report issues | Requires a tester with automation testing skills, including an understanding of programming languages and automation tools, as well as the ability to write and maintain automated test scripts| 

### Test-Driven Development

- Test Driven Development (TDD) is a software development practice where developers write automated tests before writing the actual code that needs to be tested. 
- Developers create unit test cases before developing the actual code. It is an iterative approach combining Programming, Unit Test Creation, and Refactoring.

The process follows a repetitive cycle known as **Red-Green-Refactor**.

1. **Red Phase:** First, a developer writes a test that defines a desired feature or behavior (the “Red” phase, as the test will fail initially).
2. **Green Phase:** Then, they write the minimum code necessary to pass the test (the “Green” phase).
3. **Refactor:** Finally, the code is refactored for optimization while ensuring the test still passes.

- TDD helps ensure that the codebase remains reliable and bug-free by catching errors early in the development process. 
- It promotes better design decisions, as writing tests first forces developers to think more clearly about the functionality they are implementing.

### Testing in Python

- Python offers an `assert` method to help perform simple tests on your code.
- `assert` in Python is a statement for setting sanity checks in your code.
- `assert()` checks a condition and raises an `AssertionError` if false.
- You should use asserts for debugging and testing, not for data validation or error handling.
- `raise` and `assert` are different because raise manually triggers an exception, while assert checks a condition and raises an exception automatically if the condition fails.

**TDD Example:**

- We want to build a calculator app that allows us to add, multiply, divide and subtract. Using TDD build the calculator program to meet the following requirements:

    1. Each of the operations should be able to handle integers or floats
    2. Division must always return a float. All other operations can return either an integer or float depending on the inputs
    3. Division by zero is not allowed
    4. Calculations between numbers and strings are not allowed and should produce an error

    ```python
    # test.py 
    from main import add

    # Add
    def test_add_returns_integer():
        result = add(5, 10)
        assert isinstance(result, int), "Result not an integer"
        
    def test_add_returns_correct_result():
        result = add(16, 10)
        assert (result == 26), "The result from add does not match"
        
    def test_add_returns_negative_from_negative_input():
        pass


    test_add_returns_integer()
    test_add_returns_correct_result()
    ```

    ```python
    # main.py
    def add(x, y):
        return x + y 
    ```
    
# live-code

## Structuring your questions

### 1. Provide Context for Your Question

- Briefly explain what you're working on and where you're encountering an issue.

**Example:**

    While working on Lab 5, I implemented a recursive Fibonacci function. It works correctly for small inputs but becomes extremely slow for values like fibonacci(35) or higher.

### 2. Ask Your Specific Question(s)

- Clearly state the exact question(s) you have. Use bullet points or numbers if you have more than one.

**Example:**

    My main questions are:

    Why does the function slow down so drastically for larger values?

    What’s the best way to optimize this in Python?

### 3. Suggest a Possible Solution or Hypothesis

- Explain what you think might be causing the problem, even if you’re not sure. This helps show your thought process.
- Demonstrate your thinking, even if it might be wrong.

**Example:**

    I believe the problem is due to repeated calculations for the same values in the recursion tree. I think using memoization could help.
    I tried using functools.lru_cache, but I’m unsure if I applied it correctly.

### 4. Describe What You’ve Tried So Far

- Mention any attempts you've made to fix the problem. Include resources you’ve checked (notes, documentation, Stack Overflow, etc.).

**Example:**

    I reviewed the lecture slides on dynamic programming, tried searching for Python memoization examples, and experimented with storing results in a dictionary, but couldn’t get it working properly.

### 5. Include Relevant Code

- Paste the specific part of the code or error that relates to your question. Highlight where you think the issue might be.

**Example:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))
```

    - Here's the code I’m using. I think wrapping this in a caching decorator might improve performance, but I’m not sure how to do that correctly.





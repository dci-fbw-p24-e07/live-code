# Asynchronous programming

- `async` and `await` are keywords used for asynchronous programming, primarily with the asyncio library. 
- They enable the writing of concurrent code that can handle multiple I/O-bound operations efficiently without blocking the main thread of execution.

- `async` Keyword: Used to define a coroutine, which is a special type of function that can be paused and resumed. When an `async` function is called, it returns a coroutine object instead of executing immediately. 

    ```Python
    async def my_coroutine():
        # ... asynchronous operations ...
        pass
    ```

- `await` Keyword: Used within an `async` function to pause its execution until a specific asynchronous task (another coroutine or an "awaitable" object) completes. This allows the program to yield control back to the event loop, enabling other tasks to run concurrently during the wait time.

```Python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2) # Simulate an I/O-bound operation
    print("Data Fetched")
    return {"data": "sample data"}

async def main():
    print("Start")
    data = await fetch_data() # Pause main until fetch_data completes
    print("Received", data)
    print("End")

asyncio.run(main())
```

**Event Loop:**
- At the core of `asyncio` and `async`/`await` is the event loop. It's responsible for managing and scheduling the execution of coroutines and handling I/O operations. `asyncio.run()` is commonly used to start and manage the event loop.

**`asyncio` Module:**
- Python's built-in `asyncio` module provides the necessary tools and high-level APIs for creating and managing coroutines, tasks, and event loops, facilitating the use of `async`/`await` for concurrent programming.

**How they work:**
When an `await` expression is encountered within an `async` function, the execution of that function is paused, and control is returned to the event loop. The event loop can then switch to another ready task or coroutine. Once the awaited operation completes (e.g., data is fetched, a sleep duration finishes), the paused coroutine is resumed from where it left off. This non-blocking nature is particularly beneficial for I/O-bound tasks like network requests, database queries, or file operations, as it allows the program to remain responsive while waiting for external resources.
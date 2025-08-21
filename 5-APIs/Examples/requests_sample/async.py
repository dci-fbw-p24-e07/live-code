import asyncio

# asynchronous function
async def fun():
    print("Hello")
    await asyncio.sleep(10) # Simulate an asynchronous task
    print("World")
    
# Call fun using asyncio
asyncio.run(fun())




import asyncio
async def greet():
    print ("Hello, async world!")

# Calling greet() doesn’t run it; it returns a coroutine object
# print(greet())  # Output: <coroutine object greet at ...>

# To run it, use asyncio.run()

asyncio.run(greet())  # Output: Hello, async world!
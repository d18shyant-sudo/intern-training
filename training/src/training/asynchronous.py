import asyncio
import time
# 1.simple synchronous function
async def get_value() -> str:
   await asyncio.sleep(1)
   return "Executed"
result = asyncio.run(get_value())
print(result)
# 2.comparision of sequential and concurrent execution
async def sequential() ->None:
   for _ in range(20):
      await get_value()
async def concurrent() ->None:
   await asyncio.gather(*(get_value() for _ in range(20)))
async def main() -> None:
   start  = time.perf_counter()
   await sequential()
   sequential_time = time.perf_counter() - start
   start = time.perf_counter()
   await concurrent()
   concurrent_time = time.perf_counter() - start
   print(f"Sequential execution time is {sequential_time:.2f} seconds")
   print(f"Concurrent execution time is {concurrent_time:.2f} seconds")
   print(f"The difference is {sequential_time-concurrent_time:.2f} seconds")
asyncio.run(main())
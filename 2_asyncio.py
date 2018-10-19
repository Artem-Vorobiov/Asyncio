#	Очень наглядно как движется поток"!"

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
loop.close()


# Task A: Compute factorial(2)...
# Task B: Compute factorial(2)...
# Task C: Compute factorial(2)...
# Task A: factorial(2) = 2
# Task B: Compute factorial(3)...
# Task C: Compute factorial(3)...
# Task B: factorial(3) = 6
# Task C: Compute factorial(4)...
# Task C: factorial(4) = 24
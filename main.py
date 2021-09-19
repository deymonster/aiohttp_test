import time
import asyncio

start = time.time()

def tic():
    return 'at %1.1f seconds' % (time.time() - start)

async def gr1():
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(5)
    print('gr1 ended work: {}'.format(tic()))

async def gr2():
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(5)
    print('gr2 Ended work: {}'.format(tic()))

async def gr3():
    print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(1)
    print('gr3 Ended work: {}'.format(tic()))

ioloop = asyncio.get_event_loop()
tasks = [
     ioloop.create_task(gr1()),
     ioloop.create_task(gr2()),
     ioloop.create_task(gr3())
]

ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()
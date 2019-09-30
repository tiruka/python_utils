# def g_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'

# for i in g_hello():
#     print(i)
#     # break
# g = g_hello()
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g)) # StopIteration

##########################
# def g_hello():
#     r = yield 'hello 1'
#     yield r

# g = g_hello()
# print(next(g))
# # print(next(g))
# print(g.send('hello 2'))

##########################

# def g_hello():
#     yield from 'hello 1'

# g = g_hello()
# print(next(g))
# print(next(g))

###########################

# def s_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'
#     return 'Done'

# def g_hello():
#     while True:
#         r = yield from s_hello()
#         yield r

# g = g_hello()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

###########################

# import asyncio
# import time

# loop = asyncio.get_event_loop()

# @asyncio.coroutine
# def worker():
#     print('start')
#     yield from asyncio.sleep(2)
#     # time.sleep(2)
#     print('end')

# loop.run_until_complete(asyncio.wait([worker(), worker()]))
# loop.close()
###########################

# import asyncio
# import time

# loop = asyncio.get_event_loop()


# async def worker():
#     print('start')
#     await asyncio.sleep(2)
#     # time.sleep(2)
#     print('end')

# loop.run_until_complete(asyncio.wait([worker(), worker()]))
# loop.close()

# import functools
# functools.lru_cache

###########################
# pip install aiohttp
# import asyncio
# import time
# import aiohttp
# import requests

# loop = asyncio.get_event_loop()

# # not simultaneous
# # async def hello(url):
# #     print(requests.get(url).content)
# #     print(time.time())

# # almost simultaneous
# async def hello(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#             print(response)
#             print(time.time())

# loop.run_until_complete(asyncio.wait([
#     hello("https://httpbin.org/headers"),
#     hello("https://httpbin.org/headers"),
# ]))
# loop.close()
###########################
# how to worker async function and to get the returns
# import asyncio
# import time
# import aiohttp
# import requests

# loop = asyncio.get_event_loop()

# async def hello(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#             print(response)
#             print(time.time())
#             return 'foobar'

# async def deal(n):
#     print(f'deal {n}')

# r = loop.run_until_complete(asyncio.wait([
#     # hello("https://httpbin.org/headers"),
#     deal(1),
#     # hello("https://httpbin.org/headers"),
# ]))

# for i in r:
#     print(i)
#     for j in i:
#         print(j.result())
# loop.close()

###########################
# async lock

# import asyncio
# loop = asyncio.get_event_loop()

# async def worker1(lock):
#     print('worker1 start')
#     with await lock:
#         await asyncio.sleep(2)
#     print('worker1 end')

# async def worker2(lock):
#     print('worker2 start')
#     with await lock:
#         await asyncio.sleep(2)
#     print('worker2 end')


# lock = asyncio.Lock()
# loop.run_until_complete(asyncio.wait([
#     worker1(lock),
#     worker2(lock)
# ]))
############################
# async Event
# import asyncio
# loop = asyncio.get_event_loop()

# async def worker1(event):
#     print('worker1 start')
#     await event.wait()
#     await asyncio.sleep(2)
#     print('worker1 end')

# async def worker2(event):
#     print('worker2 start')
#     await event.wait()
#     await asyncio.sleep(2)
#     print('worker2 end')

# async def worker3(event):
#     print('worker3 start')
#     await asyncio.sleep(2)
#     print('worker3 end')
#     event.set()

# event = asyncio.Event()
# loop.run_until_complete(asyncio.wait([
#     worker1(event),
#     worker2(event),
#     worker3(event)
# ]))
# ############################
# # async Condition
# import asyncio
# loop = asyncio.get_event_loop()

# async def worker1(condition):

#     with await condition:
#         condition.wait() # これがないと、lockがかからないので、worker1,2が同時に動く。
#         print('worker1 start')
#         await asyncio.sleep(2)
#     print('worker1 end')

# async def worker2(condition):
#     with await condition:
#         condition.wait() 
#         print('worker2 start')
#         await asyncio.sleep(2)
#     print('worker2 end')

# async def worker3(condition):
#     print('worker3 start')
#     with await condition:
#         await asyncio.sleep(2)
#         condition.notify_all()
#     print('worker3 end')

# condition = asyncio.Condition()
# loop.run_until_complete(asyncio.wait([
#     worker1(condition),
#     worker2(condition),
#     worker3(condition)
# ]))

############################
# async Queue
# import asyncio
# loop = asyncio.get_event_loop()

# async def worker1(queue):
#     print('worker1 start')
#     await queue.put(100)
#     print('worker1 end')

# async def worker2(queue):
#     print('worker2 start')
#     x = await queue.get()
#     print(x)
#     print('worker2 end')

# queue = asyncio.Queue()
# loop.run_until_complete(asyncio.wait([
#     worker1(queue),
#     worker2(queue),
# ]))
#############################
# Future
# import asyncio
# loop = asyncio.get_event_loop()

# async def f(future):
#     await asyncio.sleep(1)
#     future.set_result('future is done!')


# future = asyncio.Future()
# asyncio.ensure_future(f(future))
# loop.run_until_complete(future)
# print(future.result())
# loop.close()


#############################
# import asyncio
# loop = asyncio.get_event_loop()

# async def f(future):
#     await asyncio.sleep(1)
#     future.set_result('future is done!')

# def got_result(future):
#     print(future.result())
#     loop.stop()

# future = asyncio.Future()
# asyncio.ensure_future(f(future))
# future.add_done_callback(got_result)

# loop.run_forever()
# loop.close()

#############################
# call_soon, call_later
# import asyncio
# loop = asyncio.get_event_loop()

# def hello(name, loop):
#     print(f'Hello {name}')
#     loop.stop()

# loop.call_later(1, hello, "mike", loop)
# loop.call_soon(hello, "nancy", loop)
# print('foobar')
# loop.run_forever()
# loop.close()

#############################
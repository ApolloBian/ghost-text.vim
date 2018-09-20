import asyncio
import http_handler
import tcp_server


# wakeup hack for windows
async def wakeup():
    while True:
        await asyncio.sleep(1)

print('test_http_server')
loop = asyncio.get_event_loop()
h = http_handler.GhostTextHttpHandler(8765)
print('start server')
s = tcp_server.TcpServer(loop, h)

s.start()

# add wakeup HACK for windows
loop.create_task(wakeup())

try:
    loop.run_forever()
except KeyboardInterrupt as e:
    pass

s.close()
loop.close()

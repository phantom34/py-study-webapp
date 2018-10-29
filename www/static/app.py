import logging; logging.basicConfig(level = logging.INFO)

import asyncio,os,json,time

from aiohttp import web

def index(requset):
    return web.Response(body=b'<h1>Awesome</h1>')
    
@asyncio.coroutine
def init(loop):
    url = '127.0.0.1'
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),url,9090)
    logging.info('server start at %s：9000' % url)
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

from orm import create_pool, destory_pool, Model, StringField, BooleanField, IntegerField, \
                FloatField, TextField
import models

import asyncio

@asyncio.coroutine
'''test orm insert select function'''
def test(loop=None):
    try:
        yield from create_pool(loop, host='127.0.0.1', port=3306, user='root', password='root', db='test')
    except BaseException as e:
        print('create pool failed!')

    roleCol = [{'name':'Dolores','id':'1'},
               {'name':'Ford','id':'2'},
               {'name':'Maeve','id':'3'},
               {'name':'Bernard','id':'4'},
               {'name':'William','id':'5'}
              ]
    for k in range(len(roleCol)):
        v = roleCol[k]
        user = models.User(id=models.get_guid(), name=v['name'], \
                           email=v['name']+'@westworld.com',passwd=v['id'])
        yield from user.save()
    user = models.User()
    print(user.findAll())
    try:
        yield from destory_pool()
    except BaseException as e:
        print('destory pool failed!')

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()


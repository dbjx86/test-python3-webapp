import time, random
import uuid
from datetime import datetime

from orm import create_pool, destory_pool, Model, StringField, BooleanField, \
                IntegerField, FloatField, TextField

def get_guid():
    seed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    key = []
    for i in range(40):
        key.append(seed[random.randint(0, 15)])
    sid = ''.join(key)
    return sid+str(time.time())[:10]

class User(Model):
    __table__ = 'users'

    id = StringField(ddl='varchar(50)', primary_key=True, default=get_guid())
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time())

class Blogs(Model):
    __table__ = 'blogs'

    id = StringField(ddl='varchar(50)', primary_key=True, default=get_guid())
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time())

class comments(Model):
    __table__ = 'comments'

    id = StringField(ddl='varchar(50)', primary_key=True, default=get_guid())
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    content = TextField()
    created_at = FloatField(default=time.time())


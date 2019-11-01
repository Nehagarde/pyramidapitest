from pyramid.config import Configurator
from waitress import serve
from pyramid.response import Response
import sqlite3
import colander
from pyramid.view import view_config
import json

#@view_config(route_name='restapis.homeview',renderer='../templates/testingrestapi.jinja2')
@view_config(route_name='restapis.homeview',renderer='json')
def homeview(request):
    class Friend(colander.TupleSchema):
        rank = colander.SchemaNode(colander.Int(),validator=colander.Range(0,9999))
        name = colander.SchemaNode(colander.String())

    class Phone(colander.MappingSchema):
        location = colander.SchemaNode(colander.String(),validator=colander.OneOf(['home', 'work']))
        number = colander.SchemaNode(colander.String())

    class Friends(colander.SequenceSchema):
        friend = Friend()

    class Phones(colander.SequenceSchema):
        phone = Phone()

    class Person(colander.MappingSchema):
        name = colander.SchemaNode(colander.String())
        age = colander.SchemaNode(colander.Int(),validator=colander.Range(0,150))
        friends = Friends()
        phones = Phones()

    json_obj1 = {
         'name': 'keith',
         'age': '20',
         'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
         'phones': [{'location': 'home', 'number': '555-1212'},
                    {'location': 'work', 'number': '555-8989'}],
    }

    json_obj2 = {
        'age': '20',
        'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
        'phones': [{'location': 'home', 'number': '555-1212'},
                   {'location': 'work', 'number': '555-8989'}],
    }

    schema = Person()

    try:
        json_schema = schema.deserialize(json_obj1)
        #json_schema = schema.deserialize(json_obj2)
    except colander.Invalid as e:
        return str(e)
    else:
        return schema.serialize(json_obj1)



def homeview1():
    return {
         'name': 'keith',
         'age': '20',
         'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
         'phones': [{'location': 'home', 'number': '555-1212'},
                    {'location': 'work', 'number': '555-8989'}],
    }

from pyramid.config import Configurator
from waitress import serve
from pyramid.response import Response
import sqlite3
import json
import colander
from pyramid.view import view_config
import json
from restapis.schema.apivalidationschema import Person
#@view_config(route_name='restapis.homeview',renderer='../templates/testingrestapi.jinja2')
@view_config(route_name='restapis.homeview',renderer='json')
def homeview(request):


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


@view_config(route_name='restapis.colandervalidationapi',renderer='json')
def colandervalidationapi(request):
    #Success#http://localhost:6543/restapis/colandervalidationapi/neha/29/[('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')]/[{'location': 'home', 'number': '555-1212'},{'location': 'work', 'number': '555-8989'},]
    # return request.matchdict

    schema = Person()

    request.matchdict['friends'] = eval(request.matchdict['friends'])
    request.matchdict['phones'] = eval(request.matchdict['phones'])


    # request.matchdict['phones'] = list(request.matchdict['phones'])
    # Fail#http://localhost:6543/restapis/colandervalidationapi/neha/29/[('1', 'jim',356), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')]/[{'location': 'home', 'number': '555-1212'},{'location': 'work', 'number': '555-8989'},]


    json_schema = schema.deserialize(request.matchdict)
    return json_schema
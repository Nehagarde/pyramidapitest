from pyramid.config import Configurator
from waitress import serve
from pyramid.response import Response
import sqlite3
from pyramid.view import view_config

@view_config(route_name='restapis.homeview',renderer='../templates/testingrestapi.jinja2')
def homeview(request):
    return {
         'name': 'keith',
         'age': '20',
         'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
         'phones': [{'location': 'home', 'number': '555-1212'},
                    {'location': 'work', 'number': '555-8989'}],
    }



def homeview1():
    return {
         'name': 'keith',
         'age': '20',
         'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
         'phones': [{'location': 'home', 'number': '555-1212'},
                    {'location': 'work', 'number': '555-8989'}],
    }

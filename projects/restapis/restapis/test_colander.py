import colander
from restapis.views import restapis
import pytest

def test_api_using_colander():
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

    incorrect = {"bar": "foo", "foo": "bar"}
    correct1 = {
         'name': 'keith',
         'age': '20',
         'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
         'phones': [{'location': 'home', 'number': '555-1212'},
                    {'location': 'work', 'number': '555-8989'}],
    }
    correct2 = {
        'name': 'keith',
        'age': 20,
        'friends': [(1, 'jim'), (2, 'bob'), (3, 'joe'), (4, 'fred')],
        'phones': [{'location': 'home', 'number': '555-1212'},
                   {'location': 'work', 'number': '555-8989'}],
    }

    mapping1 = Person().serialize(correct2)

    assert (mapping1 == correct1)
    assert (mapping1 == correct2)   #Error

    mapping2 = Person().deserialize(correct1)
    assert (mapping2 == correct2)
    assert (mapping2 == correct1) #Error
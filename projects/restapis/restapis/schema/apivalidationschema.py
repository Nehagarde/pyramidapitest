import colander
class Friend(colander.TupleSchema):
    rank = colander.SchemaNode(colander.Int(), validator=colander.Range(0, 9999))
    name = colander.SchemaNode(colander.String())


class Phone(colander.MappingSchema):
    location = colander.SchemaNode(colander.String(), validator=colander.OneOf(['home', 'work']))
    number = colander.SchemaNode(colander.String())


class Friends(colander.SequenceSchema):
    friend = Friend()


class Phones(colander.SequenceSchema):
    phone = Phone()


class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Int(), validator=colander.Range(0, 150))
    friends = Friends()
    phones = Phones()
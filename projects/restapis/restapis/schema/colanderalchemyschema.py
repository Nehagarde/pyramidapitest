from colanderalchemy import setup_schema
from restapis.models.mymodel import Persons
setup_schema(None, Persons)
schema = Persons.__colanderalchemy__
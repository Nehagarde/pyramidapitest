from pyramid.view import view_config
from pyramid.response import Response
from collections import defaultdict

from sqlalchemy.exc import DBAPIError
from .. import models

from cornice import Service


user_info = Service(name='users',
                    path='/{username}/info',
                    description='Get and set user data.')

_USERS = defaultdict(dict)

@user_info.get()
def get_info(request):
    """Returns the public information about a **user**.

    If the user does not exists, returns an empty dataset.
    """
    username = request.matchdict['username']
    return _USERS[username]


db_err_msg = """\
Err
"""
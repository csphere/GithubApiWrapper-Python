from repos import Repos
from users import Users
from pullreq import PullReq
from events import Events
from orgs import Orgs

class Api:
    apiurl = 'https://api.github.com'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orgs = Orgs( self )
        self.pullreqs = PullReq( self )
        self.repos = Repos( self )
        self.users = Users( self )
        self.events = Events( self )
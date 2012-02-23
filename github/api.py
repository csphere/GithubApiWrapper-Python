from repos import Repos

class Api:
    apiurl = 'https://api.github.com'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.repos = Repos( self )

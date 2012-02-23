from api import Api
from http import HTTP

class Github( HTTP ):
    def __init__(self, username, password ):
        self.api = Api( username, password )
        HTTP.__init__( self, self.api )

    def execute(self, httpVerb, path, data=None):
        if httpVerb == 'HEAD':
            return self.head( path )
        elif httpVerb == 'GET':
            return self.get( path )
        elif httpVerb == 'POST':
            return self.post( path, data )
        elif httpVerb == 'PATCH':
            return self.patch( path, data )
        elif httpVerb == 'PUT':
            return self.put( path, data )
        elif httpVerb == 'DELETE':
            return self.head( path )
        else:
            raise Exception( 'Invalid httpVerb. Use: HEAD,GET,POST,PATCH,PUT, or DELETE' )
import requests, json


class HTTP( ):
    def __init__(self, api):
        self.api = api

    def head(self, path):
        url = self.__buildurl( path )
        r = requests.head( url, auth = (self.api.username, self.api.password) )
        j = json.dumps( self.__buildResponse( r ) )
        return self.indentJson( j )

    def get(self, path):
        url = self.__buildurl( path )
        r = requests.get( url, auth = (self.api.username, self.api.password) )
        j = json.dumps( self.__buildResponse( r ) )
        return self.indentJson( j )

    def post(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.post( url, data = data, auth = (self.api.username, self.api.password) )
        j = json.dumps( self.__buildResponse( r ) )
        return self.indentJson( j )

    def patch(self, path, data):
        url = self.__buildurl( path )
        r = requests.patch( url, data = data, auth = (self.api.username, self.api.password) )
        j = json.dumps( self.__buildResponse( r ) )
        return self.indentJson( j )

    def put(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.put( url, data = data, auth = (self.api.username, self.api.password) )
        j = json.dumps( self.__buildResponse( r ) )
        return self.indentJson( j )

    def delete(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.post( url, data = data, auth = (self.api.username, self.api.password) )
        j = json.dumps( self.__buildResponse( r ) )
        return self.indentJson( j )

    def __buildurl(self, path):
        from api import Api

        return Api.apiurl + (path if (path[0] is '/') else ('/%s' % path))

    def __buildResponse(self, r):
        return {
            'headers': r.headers,
            'data': json.loads( r.content )
        }

    def indentJson(self, s):
        return json.dumps( json.loads( s, ), sort_keys = True, indent = 4 )
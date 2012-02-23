import requests, json


class HTTP( ):
    def __init__(self, api):
        self.api = api

    def head(self, path):
        url = self.__buildurl( path )
        r = requests.head( url, auth = (self.api.username, self.api.password) )
        return json.dumps( self.__buildResponse( r ) )

    def get(self, path):
        url = self.__buildurl( path )
        r = requests.get( url, auth = (self.api.username, self.api.password) )
        return json.dumps( self.__buildResponse( r ) )

    def post(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.post( url, data = data, auth = (self.api.username, self.api.password) )
        return json.dumps( self.__buildResponse( r ) )

    def patch(self, path, data):
        url = self.__buildurl( path )
        r = requests.patch( url, data = data, auth = (self.api.username, self.api.password) )
        return json.dumps( self.__buildResponse( r ) )

    def put(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.put( url, data = data, auth = (self.api.username, self.api.password) )
        return json.dumps( self.__buildResponse( r ) )

    def delete(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.post( url, data = data, auth = (self.api.username, self.api.password) )
        return json.dumps( self.__buildResponse( r ) )

    def __buildurl(self, path):
        from api import Api

        return Api.apiurl + (path if (path[0] is '/') else ('/%s' % path))

    def __buildResponse(self, r):
        return {
            'headers': r.headers,
            'data': json.loads( r.content )
        }
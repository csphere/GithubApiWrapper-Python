import requests, json


class HTTP( ):
    def __init__(self, api):
        self.api = api

    def head(self, path):
        url = self.__buildurl( path )
        r = requests.head( url, auth = (self.api.username, self.api.password) )
        response = {}
        response['headers'] = r.headers
        response['data'] = json.loads( r.content )
        return json.dumps( response )

    def get(self, path):
        url = self.__buildurl( path )
        r = requests.get( url, auth = (self.api.username, self.api.password) )
        response = {}
        response['headers'] = r.headers
        response['data'] = json.loads( r.content )
        return json.dumps( response )

    def post(self, path, data):
        url = self.__buildurl( path )
        r = requests.post( url, data = data, auth = (self.api.username, self.api.password) )
        response = {}
        response['headers'] = r.headers
        response['data'] = json.loads( r.content )
        return json.dumps( response )

    def patch(self, path, data):
        url = self.__buildurl( path )
        r = requests.patch( url, data = data, auth = (self.api.username, self.api.password) )
        response = {}
        response['headers'] = r.headers
        response['data'] = json.loads( r.content )
        return json.dumps( response )

    def put(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.put( url, data = data, auth = (self.api.username, self.api.password) )
        response = {}
        response['headers'] = r.headers
        response['data'] = json.loads( r.content )
        return json.dumps( response )

    def delete(self, path):
        url = self.__buildurl( path )
        r = requests.post( url, auth = (self.api.username, self.api.password) )
        response = {}
        response['headers'] = r.headers
        response['data'] = json.loads( r.content )
        return json.dumps( response )

    def __buildurl(self, path):
        from api import Api

        return Api.apiurl + (path if (path[0] is '/') else ('/%s' % path))
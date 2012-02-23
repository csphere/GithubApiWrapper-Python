import requests

class HTTP( ):
    def __init__(self, api):
        self.api = api

    def head(self, path):
        url = self.__buildurl( path )
        r = requests.head( url, auth = (self.api.username, self.api.password) )
        return r.headers

    def get(self, path):
        url = self.__buildurl( path )
        r = requests.get( url, auth = (self.api.username, self.api.password) )
        return r.content

    def post(self, path, data):
        url = self.__buildurl( path )
        r = requests.post( url, data = data, auth = (self.api.username, self.api.password) )
        return r.content

    def patch(self, path, data):
        url = self.__buildurl( path )
        r = requests.patch( url, data = data, auth = (self.api.username, self.api.password) )
        return r.content

    def put(self, path, data=None):
        url = self.__buildurl( path )
        r = requests.put( url, data = data, auth = (self.api.username, self.api.password) )
        return r.headers

    def delete(self, path):
        url = self.__buildurl( path )
        r = requests.post( url, auth = (self.api.username, self.api.password) )
        return r.headers

    def __buildurl(self, path):
        from api import Api

        return Api.apiurl + (path if (path[0] is '/') else ('/%s' % path))
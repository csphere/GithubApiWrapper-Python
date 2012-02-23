from http import HTTP

class Forks:
    def __init__(self, api):
        self.__api = api

    def listForks(self, repo, sort=None, user=None):
        username = self.__api.username if user is None else user
        if sort:
            url = '%s?sort=%s' % ('repos/%s/%s/forks' % (username, repo), sort)
        else:
            url = 'repos/%s/%s/forks' % (username, repo)
        return HTTP( self.__api ).get( url )

    def createFork(self, repo, org=None, user=None):
        username = self.__api.username if user is None else user
        if org:
            url = '%s?%s' % ('repos/%s/%s/forks' % (username, repo), org)
        else:
            url = 'repos/%s/%s/forks' % (username, repo)
        return HTTP( self.__api ).post( url )
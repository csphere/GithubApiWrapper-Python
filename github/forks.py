from http import HTTP

class Forks:
    def __init__(self, api):
        self.__api = api

    def listForks(self, repo, sort=None, user=None):
        username = self.__api.username if user == None else user
        if sort:
            url = '%s?%s' % ('repos/%s/%s/forks' % (username, repo), sort)
        else:
            url = 'repos/%s/%s/forks' % (username, repo)
        return HTTP( self.__api ).get( url )

    def listForks(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/forks' % (username, repo), )

    def createFork(self, repo, org=None, user=None):
        username = self.__api.username if user == None else user
        if org:
            url = '%s?%s' % ('repos/%s/%s/forks' % (username, repo), org)
        else:
            url = 'repos/%s/%s/forks' % (username, repo)
        return HTTP( self.__api ).get( url )
from http import HTTP

class Watching:
    def __init__(self, api):
        self.__api = api

    def listWatchers(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/watchers' % (username, repo) )

    def listWatchedRepos(self, user=None):
        url = 'users/%s/watched' % user if (user != None and user != self.__api.username) else 'user/watched'
        return HTTP( self.__api ).get( url )

    def checkIfWatching(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'user/watched/%s/%s' % (username, repo) )

    def watchRepo(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).put( 'user/watched/%s/%s' % (username, repo) )

    def stopWatching(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).delete( 'user/watched/%s/%s' % (username, repo) )
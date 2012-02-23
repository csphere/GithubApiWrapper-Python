from http import HTTP

class Followers:
    def __init__(self, api):
        self.__api = api

    def listFollowers(self, user=None):
        url = 'users/%s/followers' % user if (user != None and user != self.__api.username) else 'user/followers'
        return HTTP( self.__api ).get( url )

    def listFollowing(self, user=None):
        url = 'users/%s/following' % user if (user != None and user != self.__api.username) else 'user/following'
        return HTTP( self.__api ).get( url )

    def listFollowing(self, user=None):
        url = 'users/%s/following' % user if (user != None and user != self.__api.username) else 'user/following'
        return HTTP( self.__api ).get( url )

    def checkIfFollowing(self, user):
        return HTTP( self.__api ).get( 'user/following/%s' % user )

    def followUser(self, user):
        return HTTP( self.__api ).put( 'user/following/%s' % user )

    def unfollowUser(self, user):
        return HTTP( self.__api ).delete( 'user/following/%s' % user )
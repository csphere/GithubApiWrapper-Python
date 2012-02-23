from http import HTTP
import json

class Keys:
    def __init__(self, api):
        self.__api = api

    def listKeys(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/keys' % (username, repo) )

    def getKey(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/keys/%s' % (username, repo, id) )

    def createKey(self, repo, title, key, user=None):
        username = self.__api.username if user == None else user
        data = json.dumps( dict(
            title = "%s" % title,
            key = "%s" % key
        ) )
        return HTTP( self.__api ).post( 'repos/%s/%s/keys' % (username, repo), data )

    def editKey(self, repo, id, title=None, key=None, user=None):
        username = self.__api.username if user == None else user

        old = json.loads( self.getKey( repo, user ) )
        new = {}
        if title and title != old['title']:
            new['title'] = title
        if key and key != old['key']:
            new['key'] = key

        data = json.dumps( new )
        return HTTP( self.__api ).post( 'repos/%s/%s/keys/%s' % (username, repo, id), data )

    def deleteKey(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).delete( 'repos/%s/%s/keys/%s' % (username, repo, id) )

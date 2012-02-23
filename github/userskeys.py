import json
from http import HTTP

class Keys:
    def __init__(self, api):
        self.__api = api

    def listPublicKeys(self):
        return HTTP( self.__api ).get( 'user/keys' )

    def getPublicKey(self, id):
        return HTTP( self.__api ).get( 'user/keys/%s' % id )

    def createPublicKey(self, title, key):
        data = json.dumps( {
            'title': title, 'key': key
        } )
        return HTTP( self.__api ).post( 'user/keys', data )

    def updatePublicKey(self, id, title, key):
        data = json.dumps( {
            'title': title, 'key': key
        } )
        return HTTP( self.__api ).patch( 'user/keys/%s' % id, data )

    def deletePublicKey(self, id):
        return HTTP( self.__api ).delete( 'user/keys/%s' % id )
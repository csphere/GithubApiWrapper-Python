import json
from http import HTTP

class Emails:
    def __init__(self, api):
        self.__api = api

    def listEmails(self):
        return HTTP( self.__api ).get( 'user/emails' )

    def addEmail(self, emails):
        data = json.dumps( emails )
        return HTTP( self.__api ).post( 'user/emails', data )

    def deleteEmail(self, emails):
        data = json.dumps( emails )
        return HTTP( self.__api ).delete( 'user/emails', data )
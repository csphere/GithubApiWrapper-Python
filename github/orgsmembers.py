from http import HTTP

class OrgsMembers:
    def __init__(self, api):
        self.__api = api

    def listMembers(self, org):
        return HTTP( self.__api ).get( 'orgs/%s/members' % org )

    def getMember(self, org, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'orgs/%s/members/%s' % (org, username) )

    def removeMember(self, org, user):
        return HTTP( self.__api ).delete( 'orgs/%s/members/%s' % (org, user) )

    def listPublicMembers(self, org):
        return HTTP( self.__api ).get( 'orgs/%s/public_members' % org )

    def getIfUserIsPublic(self, org, user):
        return HTTP( self.__api ).get( 'orgs/%s/public_members/%s' % (org, user) )

    def publicizeUser(self, org, user):
        return HTTP( self.__api ).put( 'orgs/%s/public_members/%s' % (org, user) )

    def concealUser(self, org, user):
        return HTTP( self.__api ).delete( 'orgs/%s/public_members/%s' % (org, user) )
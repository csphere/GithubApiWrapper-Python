from http import HTTP
# from eventtypes import EventTypes

class Events(  ):
    def __init__(self, api):
        # EventTypes.__init__( self )
        self.__api = api

    def listPublicEvents(self):
        return HTTP( self.__api ).get( 'events' )

    def listRepoEvents(self, repo, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/events' % (username, repo) )

    def listRepoIssueEvents(self, repo, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/issues/events' % (username, repo) )

    def listRepoNetworkPublicEvents(self, repo, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'network/%s/%s/events' % (username, repo) )

    def listOrgPublicEvents(self, org):
        return HTTP( self.__api ).get( 'orgs/%s/events' % org )

    def listRepoIssueEvents(self, repo, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/issues/events' % (username, repo) )

    def listReceivedEvents(self, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'users/%s/received_events' % username )

    def listReceivedPublicEvents(self, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'users/%s/received_events/public' % username )

    def listOrgEvents(self, org):
        username = self.__api.username
        return HTTP( self.__api ).get( 'users/%s/events/orgs/%s' % (username, org) )
from http import HTTP

class Collaborators:
    def __init__(self, api):
        self.__api = api

    def list(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/collaborators' % (username, repo) )

    def get(self, repo, collaborator, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/collaborators/%s' % (username, repo, collaborator) )

    def addCollaborator(self, repo, collaborator, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).put( 'repos/%s/%s/collaborators/%s' % (username, repo, collaborator) )

    def deleteCollaborator(self, repo, collaborator, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).delete( 'repos/%s/%s/collaborators/%s' % (username, repo, collaborator) )
import json
from http import HTTP

class ReviewComments:
    def __init__(self, api):
        self.__api = api

    def listComments(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/%s/comments' % (username, repo, id) )

    def getComment(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/comments/%s' % (username, repo, id) )

    def listComments(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/%s/comments' % (username, repo, id) )

    def createComment(self, repo, id, body, commit_id, path, position, user=None):
        username = self.__api.username if user is None else user
        data = json.dumps( {
            'body': "%s" % body,
            'commit_id': "%s" % commit_id,
            'path': "%s" % path,
            'position': position
        } )
        return HTTP( self.__api ).post( 'repos/%s/%s/pulls/%s/comments' % (username, repo, id), data )

    def createCommentResponse(self, repo, id, body, in_reply_to, user=None):
        username = self.__api.username if user is None else user
        data = json.dumps( {
            'body': "%s" % body,
            'in_reply_to': in_reply_to
        } )
        return HTTP( self.__api ).post( 'repos/%s/%s/pulls/%s/comments' % (username, repo, id), data )

    def editComment(self, repo, id, body, user=None):
        username = self.__api.username if user is None else user
        data = json.dumps( {
            'body': body
        } )
        return HTTP( self.__api ).patch( 'repos/%s/%s/pulls/comments/%s' % (username, repo, id), data )

    def deleteComment(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).delete( 'repos/%s/%s/pulls/comments/%s' % (username, repo, id) )
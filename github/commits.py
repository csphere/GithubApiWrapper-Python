import json
from http import HTTP

class Commits:
    def __init__(self, api):
        self.__api = api

    def listCommits(self, repo, sha=None, path=None, user=None):
        username = self.__api.username if user == None else user
        url = 'repos/%s/%s/commits' % (username, repo)
        if sha or path:
            url = '%s?' % url
        if sha:
            url = '%ssha=%s&' % (url, sha)
        if path:
            url = '%spath=%s&' % (url, path)
        return HTTP( self.__api ).get( url )

    def getCommit(self, repo, sha, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/commits/%s' % (username, repo, sha) )

    # shouldn't this be in Repo instead of Commits?...<twitch> http://developer.github.com/v3/repos/commits/
    def listRepoComments(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/comments' % (username, repo) )

    def listComments(self, repo, sha, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/comments/%s/comments' % (username, repo, sha) )

    def createComment(self, repo, sha, body, line, path, position, user=None):
        username = self.__api.username if user == None else user
        data = json.dumps( dict(
            body = body,
            commit_id = sha,
            line = line,
            path = path,
            position = position
        ) )
        return HTTP( self.__api ).post( 'repos/%s/%s/commits/%s/comments' % (username, repo, sha), data )

    def getSingleComment(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/comment/%s' % (username, repo, id) )

    def updateComment(self, repo, id, body, user=None):
        username = self.__api.username if user == None else user
        data = json.dumps( dict(
            body = body,
        ) )
        return HTTP( self.__api ).post( 'repos/%s/%s/comments/%s' % (username, repo, id), data )

    def CompareCommits(self, repo, base, head, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/compare/%s...:%' % (username, repo, base, head) )


    def deleteComment(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).delete( 'repos/%s/%s/comments/%s' % (username, repo, id) )
from http import HTTP
import json
from pullreqreviewcomments import ReviewComments

class PullReq:
    def __init__(self, api):
        self.__api = api
        self.reviewcomments = ReviewComments( self.__api )

    def listPullRequests(self, repo, state=None, user=None):
        username = self.__api.username if user is None else user
        url = 'repos/%s/%s/pulls' % (username, repo)
        if state:
            url = '%s?state=%s' % (url, state)
        return HTTP( self.__api ).get( url )

    def getPullRequest(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/%s' % (username, repo, id) )

    def createPullRequest(self, repo, title, base, head, body='', user=None):
        username = self.__api.username if user is None else user
        new = {
            'title': "%s" % title,
            'base': "%s" % base,
            'head': "%s" % head
        }
        if body:
            new['body'] = body
        data = json.dumps( new )
        return HTTP( self.__api ).post( 'repos/%s/%s/pulls' % (username, repo), data )

    def createPullRequestFromIssue(self, repo, issue, base, head, user=None):
        username = self.__api.username if user is None else user
        data = json.dumps( {
            'issue': "%s" % issue,
            'base': "%s" % base,
            'head': "%s" % head
        } )
        return HTTP( self.__api ).post( 'repos/%s/%s/pulls' % (username, repo), data )

    def listPullRequestCommits(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/%s/commits' % (username, repo, id) )

    def listPullRequestFiles(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/%s/files' % (username, repo, id) )

    def getIfPullRequestMerged(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/pulls/%s/merge' % (username, repo, id) )

    def mergePullRequest(self, repo, id, message='', user=None):
        username = self.__api.username if user is None else user
        if message:
            data = json.dumps( {
                'commit_message': message
            } )
            return HTTP( self.__api ).put( 'repos/%s/%s/pulls/%s/merge' % (username, repo, id), data )
        else:
            return HTTP( self.__api ).put( 'repos/%s/%s/pulls/%s/merge' % (username, repo, id) )
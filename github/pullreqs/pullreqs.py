import urllib, json
from pullreqsreviewcomments import PullReviewComments

class PullReq:
    def __init__(self, github):
        self.__github = github
        self.reviewcomments = PullReviewComments(self.__github)

    def listPullRequests(self, repo, state=None, user=None):
        username = self.__github.username if user is None else user
        url = 'repos/%s/%s/pulls' % (username, repo)
        url = '%s?%s' % (url, urllib.urlencode(state)) if state else url
        return self.__github.get(url)

    def getPullRequest(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/%s' % (username, repo, id))

    def createPullRequest(self, repo, title, base, head, body=None, user=None):
        username = self.__github.username if user is None else user
        params = {
            'title': title,
            'base': base,
            'head': head,
            'body': body
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/pulls' % (username, repo), data)

    def createPullRequestFromIssue(self, repo, issue, base, head, user=None):
        username = self.__github.username if user is None else user
        params = {
            'issue': issue,
            'base': base,
            'head': head
        }
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/pulls' % (username, repo),
                                  data)

    def listPullRequestCommits(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/%s/commits' % (username, repo, id))

    def listPullRequestFiles(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/%s/files' % (username, repo, id))

    def getIfPullRequestMerged(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/%s/merge' % (username, repo, id))

    def mergePullRequest(self, repo, id, commit_message=None, user=None):
        username = self.__github.username if user is None else user
        if commit_message:
            params = {
                'commit_message': commit_message
            }
            data = json.dumps(params)
            return self.__github.put(
                'repos/%s/%s/pulls/%s/merge' % (username, repo, id), data)
        else:
            return self.__github.put(
                'repos/%s/%s/pulls/%s/merge' % (username, repo, id))
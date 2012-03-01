import json


class ReposCommits:
    def __init__(self, github):
        self.__github = github

    def listCommits(self, repo, sha=None, path=None, user=None):
        username = self.__github.username if user is None else user
        params = {
            'sha': sha,
            'path': path
        }
        params = self.__github.__removeEmptyParams(params)
        url = 'repos/%s/%s/commits?%s' % (
            username, repo, params) if params else 'repos/%s/%s/commits'
        return self.__github.get(url)

    def getCommit(self, repo, sha, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/commits/%s' % (username, repo, sha))

    def listRepoComments(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/comments' % (username, repo))

    def listComments(self, repo, sha, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/comments/%s/comments' % (username, repo, sha))

    def createComment(self, repo, sha, body, line, path, position, user=None):
        username = self.__github.username if user is None else user
        params = {
            'body': body,
            'commit_id': sha,
            'line': line,
            'path': path,
            'position': position
        }
        data = json.dumps(params)
        return self.__github.post(
            'repos/%s/%s/commits/%s/comments' % (username, repo, sha), data)

    def getSingleComment(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/comment/%s' % (username, repo, id))

    def updateComment(self, repo, id, body, user=None):
        username = self.__github.username if user is None else user
        params = {
            'body': body
        }
        data = json.dumps(params)
        return self.__github.post(
            'repos/%s/%s/comments/%s' % (username, repo, id), data)

    def CompareCommits(self, repo, base, head, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/compare/%s...:%s' % (username, repo, base, head))


    def deleteComment(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'repos/%s/%s/comments/%s' % (username, repo, id))
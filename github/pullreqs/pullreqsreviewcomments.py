import json

class PullReviewComments:
    def __init__(self, github):
        self.__github = github

    def listComments(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/%s/comments' % (username, repo, id))

    def getComment(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/comments/%s' % (username, repo, id))

    def listComments(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/pulls/%s/comments' % (username, repo, id))

    def createComment(self, repo, id, body, commit_id, path, position,
                      user=None):
        username = self.__github.username if user is None else user
        params = {
            'body': body,
            'commit_id': commit_id,
            'path': path,
            'position': position
        }
        data = json.dumps(params)
        return self.__github.post(
            'repos/%s/%s/pulls/%s/comments' % (username, repo, id), data)

    def createCommentResponse(self, repo, id, body, in_reply_to, user=None):
        username = self.__github.username if user is None else user
        params = {
            'body': body,
            'in_reply_to': in_reply_to
        }
        data = json.dumps(params)
        return self.__github.post(
            'repos/%s/%s/pulls/%s/comments' % (username, repo, id), data)

    def editComment(self, repo, id, body, user=None):
        username = self.__github.username if user is None else user
        params = {
            'body': body
        }
        data = json.dumps(params)
        return self.__github.patch(
            'repos/%s/%s/pulls/comments/%s' % (username, repo, id), data)

    def deleteComment(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'repos/%s/%s/pulls/comments/%s' % (username, repo, id))
import json

class ReposKeys:
    def __init__(self, github):
        self.__github = github

    def listKeys(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/keys' % (username, repo))

    def getKey(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/keys/%s' % (username, repo, id))

    def createKey(self, repo, title, key, user=None):
        username = self.__github.username if user is None else user
        params = {
            'title': title,
            'key': key
        }
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/keys' % (username, repo),
                                  data)

    def editKey(self, repo, id, title=None, key=None, user=None):
        username = self.__github.username if user is None else user
        params = {
            'title': title,
            'key': key
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.patch(
            'repos/%s/%s/keys/%s' % (username, repo, id), data)

    def deleteKey(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'repos/%s/%s/keys/%s' % (username, repo, id))

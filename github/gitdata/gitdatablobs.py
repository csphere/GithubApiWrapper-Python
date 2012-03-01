import json

class GitDataBlobs:
    def __init__(self, github):
        self.__github = github

    def getBlob(self, repo, sha, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/git/blobs/%s' % (username, repo, sha))

    def createBlob(self, repo, content, encoding, user=None):
        username = self.__github.username if user is None else user
        params = {
            'content': content,
            'encoding': encoding
        }
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/git/blobs' % (username, repo),
                                  data)

        

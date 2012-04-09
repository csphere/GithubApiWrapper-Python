import json

class ReposDownloads:
    def __init__(self, github):
        self.__github = github

    def getDownloads(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/downloads' % (username, repo), )

    def getDownload(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/downloads/%s' % (username, repo, id), )

    def createNewDownload(self, repo, name, size, description=None,
                          content_type=None, user=None):
        username = self.__github.username if user is None else user
        params = {
            'name': name,
            'size': size,
            'description': description,
            'content_type': content_type
        }
        data = json.dumps(params)
        url = 'repos/%s/%s/downloads/%s' % (username, repo, id)
        resource = self.__github.post(url, data)
        jresource = json.loads(resource)
        # TODO


    def deleteDownload(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'repos/%s/%s/downloads/%s' % (username, repo, id) )
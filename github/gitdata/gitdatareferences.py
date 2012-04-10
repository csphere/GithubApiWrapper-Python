import json

class GitDataReferences:
    def __init__(self, github):
        self.__github = github

    def getReference(self, repo, ref, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/git/refs/%s' % (username, repo, ref))

    def getReferences(self, repo, subnamespace=None, user=None):
        username = self.__github.username if user is None else user
        url = 'repos/%s/%s/git/refs' % (repo, username)
        if subnamespace:
            url = '%s%s' % (url, subnamespace) if subnamespace[0] == '/' else '%s/%s' % (url, subnamespace)
        return self.__github.get(url)

    def createReference(self, repo, ref, sha, user=None):
        username = self.__github.username if user is None else user
        params = {
            'ref': ref,
            'sha': sha
        }
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/git/refs' % (username, repo),
                                  data)

    def editReference(self, repo, sha, force=False, user=None):
        username = self.__github.username if user is None else user
        params = {
            'sha': sha,
            'force': force
        }
        data = json.dumps(params)
        return self.__github.patch('repos/%s/%s/git/refs' % (username, repo),
                                   data)


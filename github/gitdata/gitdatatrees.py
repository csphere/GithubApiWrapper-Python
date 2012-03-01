import json

class GitDataTrees:
    def __init__(self, github):
        self.__github = github

    def getTree(self, repo, sha, recursive=False, user=None):
        username = self.__github.username if user is None else user
        url = 'repos/%s/%s/git/trees/%s' % (username, repo, sha)
        url = '%s?recursive=1' % url if recursive else url
        return self.__github.get(url)

    def createTree(self, repo, tree, baseTree=None, user=None):
        username = self.__github.username if user is None else user
        params = {
            'base_tree': baseTree,
            'tree': tree
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/git/trees' % (username, repo),
                                  data)
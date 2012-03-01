import urllib

class ReposForks:
    def __init__(self, github):
        self.__github = github

    def listForks(self, repo, sort=None, user=None):
        username = self.__github.username if user is None else user
        url = 'repos/%s/%s/forks' % (username, repo)
        if sort:
            url = '%s?%s' % (url, urllib.urlencode({'sort': sort}))
        return self.__github.get(url)

    def createFork(self, repo, org=None, user=None):
        username = self.__github.username if user is None else user
        url = 'repos/%s/%s/forks' % (username, repo)
        if org:
            url = '%s?%s' % (url, {'org': org})
        return self.__github.post(url)
class ReposWatching:
    def __init__(self, github):
        self.__github = github

    def listWatchers(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/watchers' % (username, repo))

    def listWatchedRepos(self, user=None):
        url = 'users/%s/watched' % user if (
            user is not None and user != self.__github.username) else 'user/watched'
        return self.__github.get(url)

    def checkIfWatching(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('user/watched/%s/%s' % (username, repo))

    def watchRepo(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.put('user/watched/%s/%s' % (username, repo))

    def stopWatching(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete('user/watched/%s/%s' % (username, repo))
class UsersFollowers:
    def __init__(self, github):
        self.__github = github

    def listFollowers(self, user=None):
        url = 'users/%s/followers' % user if (
            user is not None and user != self.__github.username) else 'user/followers'
        return self.__github.get(url)

    def listFollowing(self, user=None):
        url = 'users/%s/following' % user if (
            user is not None and user != self.__github.username) else 'user/following'
        return self.__github.get(url)

    def listFollowing(self, user=None):
        url = 'users/%s/following' % user if (
            user is not None and user != self.__github.username) else 'user/following'
        return self.__github.get(url)

    def checkIfFollowing(self, user):
        return self.__github.get('user/following/%s' % user)

    def followUser(self, user):
        return self.__github.put('user/following/%s' % user)

    def unfollowUser(self, user):
        return self.__github.delete('user/following/%s' % user)
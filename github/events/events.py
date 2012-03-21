class Events:
    def __init__(self, github):
        #TODO: Rsearch http://developer.github.com/v3/events/types/
        self.__github = github

    def listPublicEvents(self):
        return self.__github.get('events')

    def listRepoEvents(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/events' % (username, repo))

    def listRepoIssueEvents(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/issues/events' % (username, repo))

    def listRepoNetworkPublicEvents(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('network/%s/%s/events' % (username, repo))

    def listOrgPublicEvents(self, org):
        return self.__github.get('orgs/%s/events' % org)

    def listReceivedEvents(self, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('users/%s/received_events' % username)

    def listReceivedPublicEvents(self, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'users/%s/received_events/public' % username)

    def listOrgEvents(self, org):
        username = self.__github.username
        return self.__github.get('users/%s/events/orgs/%s' % (username, org))
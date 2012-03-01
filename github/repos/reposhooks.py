import json

class ReposHooks:
    def __init__(self, github):
        self.__github = github

    def listHooks(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/hooks' % (username, repo))

    def getHook(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/hooks/%s' % (username, repo, id))

    def createHook(self, repo, name, config, events=None, active=True,
                   user=None):
        username = self.__github.username if user is None else user
        params = {
            'name': name,
            'config': config,
            'events': events,
            'active': active
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/hooks' % (username, repo),
                                  data)

    def editHook(self, repo, id, name, config, events=None, add_events=None,
                 remove_events=None, active=True,
                 user=None):
        username = self.__github.username if user is None else user
        params = {
            'name': name,
            'config': config,
            'events': events,
            'add_events': add_events,
            'remove_events': remove_events,
            'active': active
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.patch(
            'repos/%s/%s/hooks/%s' % (username, repo, id), data)

    def testHook(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.post(
            'repos/%s/%s/hooks/%s/test' % (username, repo, id))

    def deleteHook(self, repo, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'repos/%s/%s/hooks/%s' % (username, repo, id))
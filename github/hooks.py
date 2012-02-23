from http import HTTP
import json

class Hooks:
    def __init__(self, api):
        self.__api = api

    def listHooks(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/hooks' % (username, repo) )

    def getHook(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/hooks/%s' % (username, repo, id) )

    def createHook(self, repo, name, config, events=[], active=True, user=None):
        username = self.__api.username if user == None else user
        data = json.dumps( dict(
            name = "%s" % name,
            config = "%s" % config,
            events = events,
            active = active
        ) )
        return HTTP( self.__api ).post( 'repos/%s/%s/hooks' % (username, repo), data )

    def editHook(self, repo, id, name, config, events=[], add_events=[], remove_events=[], active=True, user=None):
        username = self.__api.username if user == None else user

        old = json.loads( self.getHook( repo, user ) )
        new = {}
        new['name'] = name if name != old['name'] and name != None else old['name']
        new['config'] = config if config != old['config'] and config != None else old['config']
        if events:
            new['events'] = events
        else:
            if add_events:
                new['add_events'] = add_events
            if remove_events:
                new['remove_events'] = remove_events
        new['active'] = active if active != old['active'] else old['active']

        data = json.dumps( new )
        return HTTP( self.__api ).patch( 'repos/%s/%s/hooks/%s' % (username, repo, id), data )

    def testHook(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).post( 'repos/%s/%s/hooks/%s/test' % (username, repo, id) )

    def deleteHook(self, repo, id, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).delete( 'repos/%s/%s/hooks/%s' % (username, repo, id) )
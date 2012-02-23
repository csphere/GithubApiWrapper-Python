import json
from http import HTTP

class OrgsTeams:
    def __init__(self, api):
        self.__api = api

    def listTeams(self, org):
        return HTTP( self.__api ).get( 'orgs/%s/teams' % org )

    def getTeam(self, id):
        return HTTP( self.__api ).get( 'teams/%s' % id )

    def createTeam(self, org, name, repo_names=None, permission=None):
        new = {
            'name': name
        }
        if permission:
            new['permission'] = permission
        if repo_names:
            new['repo_names'] = repo_names

        data = json.dumps( new )
        return HTTP( self.__api ).post( 'orgs/%s/teams' % org, data )

    def editTeam(self, id, name, permission=None):
        new = {
            'name': name
        }
        if permission:
            new['permission'] = permission

        data = json.dumps( new )
        return HTTP( self.__api ).patch( 'teams/%s' % id, data )

    def deleteTeam(self, id):
        return HTTP( self.__api ).delete( 'teams/%s' % id )

    def listTeamMembers(self, id):
        return HTTP( self.__api ).get( 'teams/%s/members' % id )

    def getTeamMember(self, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'teams/%s/members/%s' % (id, username) )

    def addTeamMember(self, id, user):
        return HTTP( self.__api ).put( 'teams/%s/members/%s' % (id, user) )

    def deleteTeamMember(self, id, user):
        return HTTP( self.__api ).delete( 'teams/%s/members/%s' % (id, user) )

    def listTeamRepos(self, id):
        return HTTP( self.__api ).get( 'teams/%s/repos' % id )

    def getTeamRepo(self, id, user, repo):
        return HTTP( self.__api ).get( 'teams/%s/repos/%s/%s' % (id, user, repo) )

    def addTeamRepo(self, id, user, repo):
        return HTTP( self.__api ).put( 'teams/%s/repos/%s/%s' % (id, user, repo) )

    def removeTeamRepo(self, id, user, repo):
        return HTTP( self.__api ).delete( 'teams/%s/repos/%s/%s' % (id, user, repo) )
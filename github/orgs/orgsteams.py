import json

class OrgsTeams:
    def __init__(self, github):
        self.__github = github

    def listTeams(self, org):
        return self.__github.get('orgs/%s/teams' % org)

    def getTeam(self, id):
        return self.__github.get('teams/%s' % id)

    def createTeam(self, org, name, repo_names=None, permission=None):
        params = {
            'name': name,
            'repo_names': repo_names,
            'permission': permission
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)

        return self.__github.post('orgs/%s/teams' % org, data)

    def editTeam(self, id, name, permission=None):
        params = {
            'name': name,
            'permission': permission
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.patch('teams/%s' % id, data)

    def deleteTeam(self, id):
        return self.__github.delete('teams/%s' % id)

    def listTeamMembers(self, id):
        return self.__github.get('teams/%s/members' % id)

    def getTeamMember(self, id, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('teams/%s/members/%s' % (id, username))

    def addTeamMember(self, id, user):
        username = self.__github.username if user is None else user
        return self.__github.put('teams/%s/members/%s' % (id, username))

    def deleteTeamMember(self, id, user):
        username = self.__github.username if user is None else user
        return self.__github.delete('teams/%s/members/%s' % (id, username))

    def listTeamRepos(self, id):
        return self.__github.get('teams/%s/repos' % id)

    def getTeamRepo(self, id, user, repo):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'teams/%s/repos/%s/%s' % (id, username, repo))

    def addTeamRepo(self, id, user, repo):
        username = self.__github.username if user is None else user
        return self.__github.put(
            'teams/%s/repos/%s/%s' % (id, username, repo))

    def removeTeamRepo(self, id, user, repo):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'teams/%s/repos/%s/%s' % (id, username, repo))
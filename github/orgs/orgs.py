import json

from orgsmembers import OrgsMembers
from orgsteams import OrgsTeams

class Orgs:
    def __init__(self, github):
        self.__github = github
        self.members = OrgsMembers(self.__github)
        self.teams = OrgsTeams(self.__github)

    def listOrgs(self, user=None):
        username = self.__github.username if user is None else user
        url = 'users/%s/orgs' % username if user != self.__github.username else 'user/orgs'
        return self.__github.get(url)

    def getOrg(self, org):
        return self.__github.get('orgs/%s' % org)

    def editOrg(self, org, billing_email=None, company=None, email=None,
                location=None, name=None ):
        params = {
            'billing_email': billing_email,
            'company': company,
            'email': email,
            'location': location,
            'name': name
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.patch('org/%s' % org, data)
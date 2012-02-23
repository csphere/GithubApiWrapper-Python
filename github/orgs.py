from http import HTTP
import json
from orgsmembers import OrgsMembers
from orgsteams import OrgsTeams

class Orgs:
    def __init__(self, api):
        self.__api = api
        self.members = OrgsMembers( self.__api )
        self.teams = OrgsTeams( self.__api )

    def listOrgs(self, user=None):
        username = self.__api.username if user is None else user
        url = 'users/%s/orgs' % username if user != self.__api.username else 'user/orgs'
        return HTTP( self.__api ).get( url )

    def getOrg(self, org):
        return HTTP( self.__api ).get( 'orgs/%s' % org )

    def editOrg(self, org, billing_email='', company='', email='', location='', name='' ):
        old = json.loads( self.getOrg( org ) )['data']
        new = {}
        if billing_email and billing_email != old['billing_email']:
            new['billing_email'] = billing_email
        if company and company != old['company']:
            new['company'] = company
        if email and email != old['email']:
            new['email'] = email
        if location and location != old['location']:
            new['location'] = location
        if name and name != old['name']:
            new['name'] = name

        data = json.dumps( new )
        return HTTP( self.__api ).patch( 'org/%s' % org, data )
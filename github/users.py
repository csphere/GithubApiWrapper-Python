from http import HTTP
import json

class Users:
    def __init__(self, api):
        self.__api = api

    def getUser(self, user=None):
        url = 'users/%s' % user if (user != None and user != self.__api.username) else 'user'
        return HTTP( self.__api ).get( url )

    def updateUser(self, name='', email='', blog='', company='', location='', hireable=False, bio='', user=None):
        old = self.getUser( user )
        new = {}
        if name and name != old['name']:
            new['name'] = name
        if email and email != old['email']:
            new['email'] = email
        if blog and blog != old['blog']:
            new['blog'] = blog
        if company and company != old['company']:
            new['company'] = company
        if location and location != old['location']:
            new['location'] = location
        if hireable != old['hireable']:
            new['hireable'] = hireable
        if bio and bio != old['bio']:
            new['bio'] = bio

        data = json.dumps( new )
        return HTTP( self.__api ).patch( 'user', data )

    
import json

from usersemails import UsersEmails
from usersfollowers import UsersFollowers
from userskeys import UsersKeys

class Users:
    def __init__(self, github):
        self.__github = github
        self.emails = UsersEmails(self.__github)
        self.followers = UsersFollowers(self.__github)
        self.keys = UsersKeys(self.__github)

    def getUser(self, user=None):
        url = 'users/%s' % user if (
            user is not None and user != self.__github.username) else 'user'
        return self.__github.get(url)

    def updateUser(self, name=None, email=None, blog=None, company=None,
                   location=None, hireable=False, bio=None):
        params = {
            'name': name,
            'email': email,
            'blog': blog,
            'company': company,
            'location': location,
            'hireable': hireable,
            'bio': bio
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.patch('user', data)

    
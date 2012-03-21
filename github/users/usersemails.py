import json

class UsersEmails:
    def __init__(self, github):
        self.__github = github

    def listEmails(self):
        return self.__github.get('user/emails')

    def addEmails(self, emails):
        data = json.dumps(emails)
        return self.__github.post('user/emails', data)

    def deleteEmail(self, emails):
        data = json.dumps(emails)
        return self.__github.delete('user/emails', data)
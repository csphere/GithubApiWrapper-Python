import json

class UsersKeys:
    def __init__(self, github):
        self.__github = github

    def listPublicKeys(self):
        return self.__github.get('user/keys')

    def getPublicKey(self, id):
        return self.__github.get('user/keys/%s' % id)

    def createPublicKey(self, title, key):
        params = {
            'title': title,
            'key': key
        }
        data = json.dumps(params)
        return self.__github.post('user/keys', data)

    def updatePublicKey(self, id, title, key):
        params = {
            'title': title,
            'key': key
        }
        data = json.dumps(params)
        return self.__github.patch('user/keys/%s' % id, data)

    def deletePublicKey(self, id):
        return self.__github.delete('user/keys/%s' % id)
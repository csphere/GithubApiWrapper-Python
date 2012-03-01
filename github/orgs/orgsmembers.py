class OrgsMembers:
    def __init__(self, github):
        self.__github = github

    def listMembers(self, org):
        return self.__github.get('orgs/%s/members' % org)

    def getMember(self, org, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('orgs/%s/members/%s' % (org, username))

    def removeMember(self, org, user):
        username = self.__github.username if user is None else user
        return self.__github.delete('orgs/%s/members/%s' % (org, username))

    def listPublicMembers(self, org):
        return self.__github.get('orgs/%s/public_members' % org)

    def getIfUserIsPublic(self, org, user):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'orgs/%s/public_members/%s' % (org, username))

    def publicizeUser(self, org, user):
        username = self.__github.username if user is None else user
        return self.__github.put(
            'orgs/%s/public_members/%s' % (org, username))

    def concealUser(self, org, user):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'orgs/%s/public_members/%s' % (org, username))
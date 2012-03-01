class ReposCollaborators:
    def __init__(self, github):
        self.__github = github

    def list(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/collaborators' % (username, repo))

    def get(self, repo, collaborator, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/collaborators/%s' % (username, repo, collaborator))

    def addCollaborator(self, repo, collaborator, user=None):
        username = self.__github.username if user is None else user
        return self.__github.put(
            'repos/%s/%s/collaborators/%s' % (username, repo, collaborator))

    def deleteCollaborator(self, repo, collaborator, user=None):
        username = self.__github.username if user is None else user
        return self.__github.delete(
            'repos/%s/%s/collaborators/%s' % (username, repo, collaborator))
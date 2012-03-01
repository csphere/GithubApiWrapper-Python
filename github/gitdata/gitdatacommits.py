import json

class GitDataCommits:
    def __init__(self, github):
        self.__github = github

    def getCommit(self, repo, sha, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/git/commits/%s' % (username, repo, sha))

    def createCommit(self, repo, message, tree, parents, authorName=None,
                     authorEmail=None, authorDate=None, committerName=None,
                     committerEmail=None, commiterDate=None, user=None):
        username = self.__github.username if user is None else user
        author = {
            'name': authorName,
            'email': authorEmail,
            'date': authorDate,
            }
        author = self.__github.__removeEmptyParams(author)
        committer = {
            'name': committerName,
            'email': committerEmail,
            'date': commiterDate
        }
        committer = self.__github.__removeEmptyParams(committer)
        params = {
            'message': message,
            'author': author,
            'committer': committer,
            'parents': parents,
            'tree': tree
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post(
            'repos/%s/%s/git/commits' % (username, repo ), data)
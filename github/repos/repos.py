import json

from reposcollaborators import ReposCollaborators
from reposcommits import ReposCommits
from reposdownloads import ReposDownloads
from reposforks import ReposForks
from reposkeys import ReposKeys
from reposwatching import ReposWatching
from reposhooks import ReposHooks

class Repos:
    def __init__(self, github):
        self.__github = github
        self.collaborators = ReposCollaborators(self.__github)
        self.commits = ReposCommits(self.__github)
        self.downloads = ReposDownloads(self.__github)
        self.forks = ReposForks(self.__github)
        self.keys = ReposKeys(self.__github)
        self.watching = ReposWatching(self.__github)
        self.hooks = ReposHooks(self.__github)

    def listUserRepos(self, user=None):
        username = self.__github.username if user is None else user
        url = 'users/%s/repos' % username if user != self.__github.username else 'user/repos'
        return self.__github.get(url)

    def createUserRepo(self, name, description=None, homepage=None,
                       private=False, has_issues=True, has_wiki=True,
                       has_downloads=True):
        params = {
            'name': name,
            'private': private,
            'has_issues': has_issues,
            'has_wiki': has_wiki,
            'has_downloads': has_downloads,
            'description': description,
            'homepage': homepage
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post('user/repos', data)

    def listOrgRepos(self, org):
        return self.__github.get('orgs/%s/repos' % org)

    def createOrgRepo(self, org, name, description=None, homepage=None,
                      private=False, has_issues=True,
                      has_wiki=True, has_downloads=True):
        params = {
            'name': name,
            'private': private,
            'has_issues': has_issues,
            'has_wiki': has_wiki,
            'has_downloads': has_downloads,
            'description': description,
            'homepage': homepage
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post('orgs/%s/repos' % org, data)

    def getRepo(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s' % (username, repo))

    def editRepo(self, repo, name, description=None, homepage=None,
                 private=False,
                 has_issues=True, has_wiki=True, has_downloads=True,
                 user=None):
        username = self.__github.username if user is None else user
        params = {
            'name': name,
            'description': description,
            'homepage': homepage,
            'private': private,
            'has_issues': has_issues,
            'has_wiki': has_wiki,
            'has_downloads': has_downloads
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.patch('repos/%s/%s' % (username, repo), data)

    def listContributors(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/contributors' % (username, repo))

    def listLangs(self, repo, user=None ):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/languages' % (username, repo))

    def listTeams(self, repo, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/teams' % (username, repo))

    def listTags(self, repo, user=None ):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/tags' % (username, repo))

    def listBranches(self, repo, user=None ):
        username = self.__github.username if user is None else user
        return self.__github.get('repos/%s/%s/branches' % (username, repo))
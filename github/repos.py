from http import HTTP
import json
from collaborators import Collaborators
from commits import Commits
from downloads import Downloads
from forks import Forks
from keys import Keys
from watching import Watching
from hooks import Hooks

class Repos( ):
    def __init__(self, api):
        self.__api = api
        self.collaborators = Collaborators( self.__api )
        self.commits = Commits( self.__api )
        self.downloads = Downloads( self.__api )
        self.forks = Forks( self.__api )
        self.keys = Keys( self.__api )
        self.watching = Watching( self.__api )
        self.hooks = Hooks( self.__api )

    def listUserRepos(self, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'user/%s/repos' % username )

    def listOrgRepos(self, org):
        return HTTP( self.__api ).get( 'orgs/%s/repos' % org )

    def createUserRepo(self, name=None, description=None, homepage=None, private=False, has_issues=True, has_wiki=True,
                       has_downloads=True):
        data = json.dumps( dict(
            name = "%s" % name,
            description = "%s" % description,
            homepage = "%s" % homepage,
            private = private,
            has_issues = has_issues,
            has_wiki = has_wiki,
            has_downloads = has_downloads
        ) )
        return HTTP( self.__api ).post( 'user/repos', data )

    def createOrgRepo(self, org, name=None, description=None, homepage=None, private=False, has_issues=True,
                      has_wiki=True, has_downloads=True):
        data = json.dumps( dict(
            name = "%s" % name,
            description = "%s" % description,
            homepage = "%s" % homepage,
            private = private,
            has_issues = has_issues,
            has_wiki = has_wiki,
            has_downloads = has_downloads
        ) )
        return HTTP( self.__api ).post( 'orgs/%s/repos' % (org, data) )

    def getRepo(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s' % (username, repo) )

    def editRepo(self, repo, user=None, name=None, description=None, homepage=None, private=False,
                 has_issues=True, has_wiki=True, has_downloads=True):
        username = self.__api.username if user == None else user

        old = json.loads( HTTP( self.__api ).get( 'repos/%s/%s' % (username, repo) ) )
        new = {}
        new['name'] = name if name != old['name'] and name != None else old['name']
        if description and description != old['description']:
            new['description'] = description
        if homepage and homepage != old['homepage']:
            new['homepage'] = homepage
        if private != old['private']:
            new['private'] = private
        if has_issues != old['has_issues']:
            new['has_issues'] = has_issues
        if has_wiki != old['has_wiki']:
            new['has_wiki'] = has_wiki
        if has_downloads != old['has_downloads']:
            new['has_downloads'] = has_downloads

        data = json.dumps( new )
        return HTTP( self.__api ).patch( 'repos/%s/%s' % (username, repo), data )

    def listContributors(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/contributors' % (username, repo) )

    def listLangs(self, repo, user=None ):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/languages' % (username, repo) )

    def listTeams(self, repo, user=None):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/teams' % (username, repo) )

    def listTags(self, repo, user=None ):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/tags' % (username, repo) )

    def listBranches(self, repo, user=None ):
        username = self.__api.username if user == None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/branches' % (username, repo) )
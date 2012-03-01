import json
import requests
from issues import issues
from pullreqs import pullreqs
from events import events
from orgs import orgs
from users import users
from repos import repos

class Github:
    apiurl = 'https://api.github.com'

    def __init__(self, username, password ):
        self.username = username
        self.password = password
        self.issues = issues.Issues(self)
        self.orgs = orgs.Orgs(self)
        self.pullreqs = pullreqs.PullReq(self)
        self.repos = repos.Repos(self)
        self.users = users.Users(self)
        self.events = events.Events(self)

    def execute(self, httpVerb, path, data=None):
        verb = str.upper(httpVerb)
        url = self.__buildurl(path)
        if verb == 'HEAD':
            return self.head(url)
        elif verb == 'GET':
            return self.get(url)
        elif verb == 'POST':
            return self.post(url, data)
        elif verb == 'PATCH':
            return self.patch(url, data)
        elif verb == 'PUT':
            return self.put(url, data)
        elif verb == 'DELETE':
            return self.head(url)
        else:
            raise Exception(
                'Invalid httpVerb. Use: head, get, post, patch, put, delete')


    def head(self, url):
        url = self.__buildurl(url)
        r = requests.head(url, auth = (self.username, self.password))
        return json.dumps(self.__buildResponse(r))

    def get(self, url):
        url = self.__buildurl(url)
        r = requests.get(url, auth = (self.username, self.password))
        return json.dumps(self.__buildResponse(r))

    def post(self, url, data=None):
        url = self.__buildurl(url)
        r = requests.post(url, data = data,
                          auth = (self.username, self.password))
        return json.dumps(self.__buildResponse(r))

    def patch(self, url, data):
        url = self.__buildurl(url)
        r = requests.patch(url, data = data,
                           auth = (self.username, self.password))
        return json.dumps(self.__buildResponse(r))

    def put(self, url, data=None):
        url = self.__buildurl(url)
        r = requests.put(url, data = data,
                         auth = (self.username, self.password))
        return json.dumps(self.__buildResponse(r))

    def delete(self, url, data=None):
        url = self.__buildurl(url)
        r = requests.post(url, data = data,
                          auth = (self.username, self.password))
        return json.dumps(self.__buildResponse(r))

    def __removeEmptyParams(self, params):
        for i in range(0, len(params)):
            if not params[i]:
                del params[i]
        return params

    def __buildurl(self, path):
        return Github.apiurl + (path if (path[0] is '/') else ('/%s' % path))

    def __buildResponse(self, response):
        return {
            'headers': response.headers,
            'data': json.loads(response.content)
        }
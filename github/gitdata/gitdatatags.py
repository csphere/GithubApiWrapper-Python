import json

class GitDataTags:
    def __init__(self, github):
        self.__github = github

    def getTag(self, repo, sha, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/git/tags/%s' % (username, repo, sha))

    def createTagObject(self, repo, tag, message, object, type, taggerName,
                        taggerEmail, taggerDate, user=None):
        username = self.__github.username if user is None else user
        tagger = {
            'name': taggerName,
            'email': taggerEmail,
            'date': taggerDate
        }
        params = {
            'tag': tag,
            'message': message,
            'object': object,
            'type': type,
            'tagger': tagger
        }
        data = json.dumps(params)
        url = 'repos/%s/%s/git/tags' % (user, repo)
        return self.__github.post(url % (username, repo), data)
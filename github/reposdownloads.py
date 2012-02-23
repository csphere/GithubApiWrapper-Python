from http import HTTP
import json
# http://wiki.woodpecker.org.cn/moin/PyCurl?action=AttachFile&do=view&target=pycurl-7.20.1-bin-win32-py26.zip

class Downloads:
    def __init__(self, api):
        self.__api = api

    def getDownloads(self, repo, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/downloads' % (username, repo), )

    def getSingleDownload(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).get( 'repos/%s/%s/downloads/%s' % (username, repo, id), )

    def createNewDownload(self, repo, name, size, description=None, content_type=None, user=None):
        username = self.__api.username if user is None else user
        data = json.dumps( dict(
            name = "%s" % name,
            size = size,
            description = "%s" % description,
            content_type = content_type
        ) )

        newResource = json.loads( HTTP( self.__api ).post( 'repos/%s/%s/downloads/%s' % (username, repo, id), data ) )
        # use pycurl / curl here to create the download... issues on windows ugh
        #     http://developer.github.com/v3/repos/downloads/     <-- "Create a new download (Part 2...)
        #     http://pycurl.sourceforge.net/

    def deleteDownload(self, repo, id, user=None):
        username = self.__api.username if user is None else user
        return HTTP( self.__api ).delete( 'repos/%s/%s/downloads/%s' % (username, repo, id), )
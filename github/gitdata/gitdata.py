from gitdatablobs import GitDataBlobs
from gitdatacommits import GitDataCommits
from gitdatareferences import GitDataReferences
from gitdatatags import GitDataTags
from gitdatatrees import GitDataTrees

class GitData:
    def __init__(self, github):
        self.__github = github
        self.blobs = GitDataBlobs(self.__github)
        self.commits = GitDataCommits(self.__github)
        self.references = GitDataReferences(self.__github)
        self.tags = GitDataTags(self.__github)
        self.trees = GitDataTrees(self.__github)
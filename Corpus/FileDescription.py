from os.path import isfile


class FileDescription:

    __path: str
    __extension: str
    __index: int

    def __init__(self,
                 path: str,
                 extensionOrFileName: str,
                 index: int = None):
        self.__path = path
        if index is None:
            self.__extension = extensionOrFileName[extensionOrFileName.rindex('.') + 1:]
            self.__index = int(extensionOrFileName[0 : extensionOrFileName.rindex('.')])
        else:
            self.__extension = extensionOrFileName
            self.__index = index

    def getPath(self) -> str:
        return self.__path

    def getIndex(self) -> int:
        return self.__index

    def getExtension(self) -> str:
        return self.__extension

    def getFileName(self,
                    thisPath=None,
                    extension=None) -> str:
        if thisPath is None:
            thisPath = self.__path
        return self.getFileNameWithIndex(thisPath,
                                         self.__index,
                                         extension)

    def getFileNameWithExtension(self, extension: str) -> str:
        return self.getFileName(self.__path, extension)

    def getFileNameWithIndex(self,
                             thisPath: str,
                             index: int,
                             extension=None) -> str:
        if extension is None:
            extension = self.__extension
        return "%s/%04d.%s" % (thisPath, index, extension)

    def getRawFileName(self) -> str:
        return "%04d.%s" % (self.__index, self.__extension)

    def addToIndex(self, count: int):
        self.__index += count

    def nextFileExists(self,
                       count: int,
                       thisPath=None):
        if thisPath is None:
            thisPath = self.__path
        return isfile(self.getFileNameWithIndex(thisPath, self.__index + count))

    def previousFileExists(self,
                           count: int,
                           thisPath=None):
        if thisPath is None:
            thisPath = self.__path
        return isfile(self.getFileNameWithIndex(thisPath, self.__index - count))

    def __repr__(self):
        return f"{self.__path} {self.__index}.{self.__extension}"

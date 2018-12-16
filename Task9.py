import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''

    def __init__(self, message):
        super(FileSystemError, self).__init__(message)

class FSItem(object):

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        if self.isfile() or self.isdirectory():
            os.rename(self.path, newname)
        else:
             raise FileSystemError("{0} item not exists ".
                                      format(self.path))

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        if os.path.exists(self.path):
            raise FileSystemError("item with name {0} already exists".
                                      format(self.path))
        else:
            if self.path[-1] == '/':
                os.makedirs(self.path)
            else:
                if self.path.rfind('/') > 0:
                    os.makedirs(self.path[0:self.path.rfind('/')])
                f = open(self.path, "w")
                f.close()


    def getname(self):
        ''' Returns name of current item '''
        return self.path

    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        return os.path.isfile(self.path)


    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        return os.path.isdir(self.path)



class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''
        super().__init__(path)
        if super().isdirectory():
            raise FileSystemError("directory with name {0} already exists".
                                      format(self.path))


    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        return os.path.getsize(self.path)

    def putcontent(self, content):
        f = open(self.path, 'a')
        f.write(content)
        f.close()


    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        with open(self.path, 'r') as f:
            return f.readlines()

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError(message='File does not exist')
        for line in self.getcontent():
            yield line


class Directory(FSItem):
    ''' Class for working with directories '''
    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory with the same path '''
        super().__init__(path)
        if super().isfile():
            raise FileSystemError("file with name {0} already exists".
                                      format(self.path))



    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not super().isdirectory():
            raise FileSystemError("directory with name {0} does not exists".
                                      format(self.path))
        for path in os.listdir(self.path):
            yield FSItem(path)


    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not super().isdirectory():
            raise FileSystemError("directory with name {0} does not exists".
                                      format(self.path))
        for path in os.listdir(self.path):
            if os.path.isfile(self.path + "/" + path):
                yield File(path)


    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not super().isdirectory():
            raise FileSystemError("directory with name {0} does not exists".
                                      format(self.path))
        if os.path.exists ( self .path):
            for name in os.listdir ( self .path):
                if os.path.isdir (os.path.join ( self .path, name)):
                    yield Directory (os.path.join ( self .path, name))



    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        if not super().isdirectory():
            raise FileSystemError("directory with name {0} does not exists".
                                      format(self.path))
        for root, dir, files in os.walk(self.path):
            for file in files:
                yield File(file)


    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        if not super().isdirectory():
            raise FileSystemError("directory with name {0} does not exists".
                                      format(self.path))
        if not os.path.isdir(self.path + "/" + name):
            raise FileSystemError("{0} is not a subdirectory".
                                      format(self.path + "/" + name))
        return Directory(self.path + "/" + name)

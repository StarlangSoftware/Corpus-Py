import unittest

from Corpus.FileDescription import FileDescription


class FileDescriptionTest(unittest.TestCase):

    def test_GetIndex(self):
        fileDescription = FileDescription("mypath", "1234.train")
        self.assertEqual(1234, fileDescription.getIndex())
        fileDescription = FileDescription("mypath", "0000.test")
        self.assertEqual(0, fileDescription.getIndex())
        fileDescription = FileDescription("mypath", "0003.dev")
        self.assertEqual(3, fileDescription.getIndex())
        fileDescription = FileDescription("mypath", "0020.train")
        self.assertEqual(20, fileDescription.getIndex())
        fileDescription = FileDescription("mypath", "0304.dev")
        self.assertEqual(304, fileDescription.getIndex())
    
    def test_GetExtension(self):
        fileDescription = FileDescription("mypath", "1234.train")
        self.assertEqual("train", fileDescription.getExtension())
        fileDescription = FileDescription("mypath", "0000.test")
        self.assertEqual("test", fileDescription.getExtension())
        fileDescription = FileDescription("mypath", "0003.dev")
        self.assertEqual("dev", fileDescription.getExtension())

    def test_GetFileName(self):
        fileDescription = FileDescription("mypath", "0003.train")
        self.assertEqual("mypath/0003.train", fileDescription.getFileName())
        self.assertEqual("newpath/0003.train", fileDescription.getFileName("newpath"))
        self.assertEqual("newpath/0000.train", fileDescription.getFileNameWithIndex("newpath", 0))
        self.assertEqual("newpath/0020.train", fileDescription.getFileNameWithIndex("newpath", 20))
        self.assertEqual("newpath/0103.train", fileDescription.getFileNameWithIndex("newpath", 103))
        self.assertEqual("newpath/0000.dev", fileDescription.getFileNameWithIndex("newpath", 0, "dev"))
        self.assertEqual("newpath/0020.dev", fileDescription.getFileNameWithIndex("newpath", 20, "dev"))
        self.assertEqual("newpath/0103.dev", fileDescription.getFileNameWithIndex("newpath", 103, "dev"))

if __name__ == '__main__':
    unittest.main()

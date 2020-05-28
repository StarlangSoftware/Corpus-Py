import unittest

from Dictionary.Word import Word

from Corpus.Sentence import Sentence


class SentenceTest(unittest.TestCase):

    sentence: Sentence

    def setUp(self) -> None:
        self.sentence = Sentence()
        self.sentence.addWord(Word("ali"))
        self.sentence.addWord(Word("topu"))
        self.sentence.addWord(Word("at"))
        self.sentence.addWord(Word("mehmet"))
        self.sentence.addWord(Word("ayşeyle"))
        self.sentence.addWord(Word("gitti"))

    def test_GetWord(self):
        self.assertEqual(Word("ali"), self.sentence.getWord(0))
        self.assertEqual(Word("at"), self.sentence.getWord(2))
        self.assertEqual(Word("gitti"), self.sentence.getWord(5))

    def test_GetIndex(self):
        self.assertEqual(0, self.sentence.getIndex(Word("ali")))
        self.assertEqual(2, self.sentence.getIndex(Word("at")))
        self.assertEqual(5, self.sentence.getIndex(Word("gitti")))

    def test_WordCount(self):
        self.assertEqual(6, self.sentence.wordCount())

    def test_CharCount(self):
        self.assertEqual(27, self.sentence.charCount())


if __name__ == '__main__':
    unittest.main()

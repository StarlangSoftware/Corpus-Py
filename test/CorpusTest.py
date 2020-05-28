import unittest

from Dictionary.Word import Word

from Corpus.Corpus import Corpus


class CorpusTest(unittest.TestCase):

    simpleCorpus: Corpus
    corpus: Corpus

    def setUp(self) -> None:
        self.corpus = Corpus("../corpus.txt")
        self.simpleCorpus = Corpus("../simplecorpus.txt")

    def test_NumberOfWords(self):
        self.assertEqual(826680, self.corpus.numberOfWords())
        self.assertEqual(24, self.simpleCorpus.numberOfWords())

    def test_Contains(self):
        self.assertTrue(self.corpus.contains("atatürk"))
        for word in self.corpus.getWordList():
            self.assertTrue(self.corpus.contains(word.getName()))
        self.assertTrue(self.simpleCorpus.contains("mehmet"))
        for word in self.simpleCorpus.getWordList():
            self.assertTrue(self.simpleCorpus.contains(word.getName()))

    def test_WordCount(self):
        self.assertEqual(98199, self.corpus.wordCount())
        self.assertEqual(12, self.simpleCorpus.wordCount())

    def test_GetCount(self):
        self.assertEqual(309, self.corpus.getCount(Word("mustafa")))
        self.assertEqual(109, self.corpus.getCount(Word("kemal")))
        self.assertEqual(122, self.corpus.getCount(Word("atatürk")))
        self.assertEqual(4, self.simpleCorpus.getCount(Word("ali")))
        self.assertEqual(3, self.simpleCorpus.getCount(Word("gitti")))
        self.assertEqual(4, self.simpleCorpus.getCount(Word("at")))

    def test_SentenceCount(self):
        self.assertEqual(50000, self.corpus.sentenceCount())
        self.assertEqual(5, self.simpleCorpus.sentenceCount())

    def test_MaxSentenceLength(self):
        self.assertEqual(1092, self.corpus.maxSentenceLength())
        self.assertEqual(6, self.simpleCorpus.maxSentenceLength())

if __name__ == '__main__':
    unittest.main()

import unittest

from Corpus.CorpusStream import CorpusStream


class CorpusTest(unittest.TestCase):

    def test_NumberOfWords1(self):
        word_count = 0
        corpus_stream = CorpusStream("../corpus.txt")
        corpus_stream.open()
        sentence = corpus_stream.getSentence()
        while sentence is not None:
            word_count = word_count + sentence.wordCount()
            sentence = corpus_stream.getSentence()
        corpus_stream.close()
        self.assertEqual(826680, word_count)

    def test_NumberOfWords2(self):
        word_count = 0
        corpus_stream = CorpusStream("../corpus.txt")
        corpus_stream.open()
        sentences = corpus_stream.getSentenceBatch(100)
        while len(sentences) != 0:
            for sentence in sentences:
                word_count = word_count + sentence.wordCount()
            sentences = corpus_stream.getSentenceBatch(100)
        corpus_stream.close()
        self.assertEqual(826680, word_count)

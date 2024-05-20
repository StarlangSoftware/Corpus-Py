from typing import IO

from Corpus.AbstractCorpus import AbstractCorpus
from Corpus.Sentence import Sentence


class CorpusStream(AbstractCorpus):

    file: IO

    def __init__(self, fileName=None):
        """
        Constructor for CorpusStream. CorpusStream is used for reading very large corpora that does not fit in memory as
        a whole. For that reason, sentences are read one by one.
        :param fileName: File name of the corpus stream.
        """
        self.file_name = fileName

    def open(self):
        """
        Implements open method in AbstractCorpus. Initializes file reader.
        """
        self.file = open(self.file_name, "r", encoding='utf8')

    def close(self):
        """
        Implements close method in AbstractCorpus. Closes the file reader.
        """
        self.file.close()

    def getNextSentence(self) -> Sentence:
        """
        Implements getSentence method in AbstractCorpus. Reads from the file buffer next sentence and returns it. If
        there are no sentences to be read, returns None.
        :return: Next read sentence from file buffer or None.
        """
        line = self.file.readline()
        if line:
            return Sentence(line.strip())
        else:
            return None

    def getSentenceBatch(self, lineCount: int) -> list:
        """
        Reads more than one line (lineCount lines) from the buffer, stores them in an array list and returns that
        array list. If there are no lineCount lines to be read, the method reads only available lines and returns them.
        :param lineCount: Maximum number of lines to read.
        :return: An array list of read lines.
        """
        sentences = []
        for i in range(lineCount):
            line = self.file.readline()
            if line:
                sentences.append(Sentence(line.strip()))
            else:
                break
        return sentences

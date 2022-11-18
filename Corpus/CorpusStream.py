from typing import IO

from Corpus.AbstractCorpus import AbstractCorpus
from Corpus.Sentence import Sentence


class CorpusStream(AbstractCorpus):

    file: IO

    def __init__(self, fileName=None):
        self.file_name = fileName

    def open(self):
        self.file = open(self.file_name, "r", encoding='utf8')

    def close(self):
        self.file.close()

    def getNextSentence(self) -> Sentence:
        line = self.file.readline()
        if line:
            return Sentence(line)
        else:
            return None

    def getSentenceBatch(self, lineCount: int) -> list:
        sentences = []
        for i in range(lineCount):
            line = self.file.readline()
            if line:
                sentences.append(Sentence(line.strip()))
            else:
                break
        return sentences

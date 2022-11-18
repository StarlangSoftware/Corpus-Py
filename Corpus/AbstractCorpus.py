from abc import abstractmethod
from Corpus.Sentence import Sentence


class AbstractCorpus:

    file_name: str

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def getNextSentence(self) -> Sentence:
        pass

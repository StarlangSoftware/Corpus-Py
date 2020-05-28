from abc import abstractmethod


class SentenceSplitter:

    SEPARATORS = "()[]{}\"'\u05F4\uFF02\u055B"
    SENTENCE_ENDERS = ".?!…"
    PUNCTUATION_CHARACTERS = ",:;"

    @abstractmethod
    def split(self, line: str) -> list:
        pass

from abc import abstractmethod


class LanguageChecker:

    @abstractmethod
    def isValidWord(self, word: str) -> bool:
        pass

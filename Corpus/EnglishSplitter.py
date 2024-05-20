from Corpus.SentenceSplitter import SentenceSplitter
from Language.EnglishLanguage import EnglishLanguage


class EnglishSplitter(SentenceSplitter):

    def upperCaseLetters(self) -> str:
        """
        Returns English UPPERCASE letters.
        :return: English UPPERCASE letters.
        """
        return EnglishLanguage.UPPERCASE_LETTERS

    def lowerCaseLetters(self) -> str:
        """
        Returns English LOWERCASE letters.
        :return: English LOWERCASE letters.
        """
        return EnglishLanguage.LOWERCASE_LETTERS

    def shortCuts(self) -> list:
        """
        Returns shortcut words in English language.
        :return: Shortcut words in English language.
        """
        return ["dr", "prof", "org", "II", "III", "IV", "VI", "VII", "VIII", "IX",
                "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
                "XX", "min", "km", "jr", "mrs", "sir"]

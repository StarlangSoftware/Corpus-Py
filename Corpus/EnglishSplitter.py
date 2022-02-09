from Corpus.SentenceSplitter import SentenceSplitter
from Language.EnglishLanguage import EnglishLanguage


class EnglishSplitter(SentenceSplitter):

    def upperCaseLetters(self) -> str:
        return EnglishLanguage.UPPERCASE_LETTERS

    def lowerCaseLetters(self) -> str:
        return EnglishLanguage.LOWERCASE_LETTERS

    def shortCuts(self) -> list:
        return ["dr", "prof", "org", "II", "III", "IV", "VI", "VII", "VIII", "IX",
                "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
                "XX", "min", "km", "jr", "mrs", "sir"]

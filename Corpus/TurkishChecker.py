from Language.TurkishLanguage import TurkishLanguage

from Corpus.LanguageChecker import LanguageChecker
from Corpus.SentenceSplitter import SentenceSplitter


class TurkishChecker(LanguageChecker):
    def isValidWord(self, word: str) -> bool:
        """
        The isValidWord method takes an input String as a word than define all valid characters as a validCharacters
        string which has letters (abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ),
        extended language characters (âàáäãèéêëíîòóôûúqwxÂÈÉÊËÌÒÛQWX),
        digits (0123456789),
        separators ({@literal ()[]{}"'״＂՛}),
        sentence enders (.?!…),
        arithmetic chars (+-=*\\),
        punctuation chars (,:;),
        special-meaning chars

        Then, loops through input word's each char and if a char in word does not in the validCharacters string it
        returns false, true otherwise.

        PARAMETERS
        ----------
        word : str
            String to check validity.

        RETURNS
        -------
        bool
            True if each char in word is valid, False otherwise.
        """
        specialMeaningCharacters = "$\\_|@%#£§&><"
        validCharacters = TurkishLanguage.LETTERS + TurkishLanguage.EXTENDED_LANGUAGE_CHARACTERS + \
                          TurkishLanguage.DIGITS + SentenceSplitter.SEPARATORS + SentenceSplitter.SENTENCE_ENDERS + \
                          TurkishLanguage.ARITHMETIC_CHARACTERS + SentenceSplitter.PUNCTUATION_CHARACTERS + \
                          specialMeaningCharacters
        for i in range(len(word)):
            if word[i] not in validCharacters:
                return False
        return True

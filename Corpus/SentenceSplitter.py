from abc import abstractmethod
import re

from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from Language.Language import Language


class SentenceSplitter:
    SEPARATORS = "\n()[]{}\"'\u05F4\uFF02\u055B’”‘“–­​	&  ﻿"
    SENTENCE_ENDERS = ".?!…"
    PUNCTUATION_CHARACTERS = ",:;‚"
    APOSTROPHES = "'’‘\u055B"

    @abstractmethod
    def upperCaseLetters(self) -> str:
        pass

    @abstractmethod
    def lowerCaseLetters(self) -> str:
        pass

    @abstractmethod
    def shortCuts(self) -> list:
        pass

    def __listContains(self, currentWord: str) -> bool:
        """
        The listContains method has a String array shortcuts which holds the possible abbreviations that might end with
        a '.' but not a sentence finisher word. It also takes a String as an input and loops through the shortcuts array
        and returns true if given String has any matching item in the shortcuts array.

        PARAMETERS
        ----------
        currentWord : str
            String input to check.

        RETURNS
        -------
        bool
            True if contains any abbreviations, False otherwise.
        """
        return currentWord in self.shortCuts()

    def __isNextCharUpperCaseOrDigit(self,
                                     line: str,
                                     i: int) -> bool:
        """
        The isNextCharUpperCaseOrDigit method takes a String line and an int i as inputs. First it compares each char in
        the input line with " " and SEPARATORS ({@literal ()[]{}"'״＂՛}) and increment i by one until a mismatch or end
        of line.

        When i equals to line length or contains one of the uppercase letters or digits it returns true, false
        otherwise.

        PARAMETERS
        ----------
        line : str
            String to check.
        i : int
            defining starting index.

        RETURNS
        -------
        bool
            True if next char is uppercase or digit, False otherwise.
        """
        while i < len(line) and (line[i] == ' ' or line[i] in SentenceSplitter.SEPARATORS):
            i = i + 1
        if i == len(line) or line[i] in self.upperCaseLetters() + Language.DIGITS + "-":
            return True
        else:
            return False

    def __isPreviousWordUpperCase(self,
                                  line: str,
                                  i: int) -> bool:
        """
        The isPreviousWordUpperCase method takes a String line and an int i as inputs. First it compares each char in
        the input line with " " and checks each char whether they are lowercase letters or one of the qxw. And decrement
        input i by one till this condition is false.

        When i equals to -1 or contains one of the uppercase letters or one of the QXW it returns true, false otherwise.

        PARAMETERS
        ----------
        line : str
            String to check.
        i : int
            defining ending index.

        RETURNS
        -------
        bool
            True if previous char is uppercase or one of the QXW, False otherwise.
        """
        while i >= 0 and (line[i] == ' ' or line[i] in self.lowerCaseLetters() + "qxw"):
            i = i - 1
        if i == -1 or line[i] in self.upperCaseLetters() + "QWX":
            return True
        else:
            return False

    def __isNextCharUpperCase(self,
                              line: str,
                              i: int) -> bool:
        """
        The isNextCharUpperCase method takes a String line and an int i as inputs. First it compares each char in
        the input line with " " and increment i by one until a mismatch or end of line.

        When i equals to line length or contains one of the uppercase letters it returns true, false otherwise.

        PARAMETERS
        ----------
        line : str
            String to check.
        i : int
            defining starting index.

        RETURNS
        -------
        bool
            True if next char is uppercase, False otherwise.
        """
        while i < len(line) and line[i] == ' ':
            i = i + 1
        if i == len(line) or line[i] in self.upperCaseLetters() + "\"\'":
            return True
        else:
            return False

    def __isNameShortcut(self, currentWord: str) -> bool:
        """
        The isNameShortcut method takes a String word as an input. First, if the word length is 1, and currentWord
        contains UPPERCASE_LETTERS letters than it returns true.

        Secondly, if the length of the word is 3 (i.e it is a shortcut) and it has a '.' at its 1st index and
        currentWord's 2nd  index is an uppercase letter it also returns true. (Ex : m.A)

        PARAMETERS
        ----------
        currentWord : str
            String input to check whether it is a shortcut.

        RETURNS
        -------
        bool
            True if given input is a shortcut, False otherwise.
        """
        if len(currentWord) == 1 and currentWord in self.upperCaseLetters():
            return True
        if len(currentWord) == 3 and currentWord[1] == '.' and currentWord[2] in self.upperCaseLetters():
            return True
        return False

    def __repeatControl(self,
                        word: str,
                        exceptionMode: bool) -> str:
        """
        The repeatControl method takes a String word as an input, and a boolean exceptionMode and compress the
        repetitive chars. With the presence of exceptionMode it directly returns the given word. Then it declares a
        counter i and loops till the end of the given word. It compares the char at index i with the char at index (i+2)
        if they are equal then it compares the char at index i with the char at index (i+1) and increments i by one and
        returns concatenated result String with char at index i.

        PARAMETERS
        ----------
        word : str
            String input.
        exceptionMode : bool
            boolean input for exceptional cases.

        RETURNS
        -------
        str
            String result.
        """
        if exceptionMode:
            return word
        i = 0
        result = ""
        while i < len(word):
            if i < len(word) - 2 and word[i] == word[i + 1] and word[i] == word[i + 2]:
                while i < len(word) - 1 and word[i] == word[i + 1]:
                    i = i + 1
            result = result + word[i]
            i = i + 1
        return result

    def __isApostrophe(self,
                       line: str,
                       i: int) -> bool:
        """
        The isApostrophe method takes a String line and an integer i as inputs. Initially declares a String
        apostropheLetters which consists of abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ,
        âàáäãèéêëíîòóôûúqwxÂÈÉÊËÌÒÛQWX and  0123456789. Then, it returns true if the result of contains method which
        checks the existence of previous char and next char at apostropheLetters returns true, returns false otherwise.

        PARAMETERS
        ----------
        line : str
            String input to check.
        i : int
            index.

        RETURNS
        -------
        bool
            True if apostropheLetters contains previous char and next char, False otherwise.
        """
        apostrophe_letters = self.upperCaseLetters() + self.lowerCaseLetters() + Language.EXTENDED_LANGUAGE_CHARACTERS \
                             + Language.DIGITS
        if i > 0 and i + 1 < len(line):
            previous_char = line[i - 1]
            next_char = line[i + 1]
            return previous_char in apostrophe_letters and next_char in apostrophe_letters
        else:
            return False

    def __numberExistsBeforeAndAfter(self,
                                     line: str,
                                     i: int) -> bool:
        """
        The numberExistsBeforeAndAfter method takes a String line and an integer i as inputs. Then, it returns true if
        the result of contains method, which compares the previous char and next char with 0123456789, returns true and
        false otherwise.

        PARAMETERS
        ----------
        line : str
            String input to check.
        i : int
            index.

        RETURNS
        -------
        bool
            True if previous char and next char is a digit, False otherwise.
        """
        if i > 0 and i + 1 < len(line):
            previous_char = line[i - 1]
            next_char = line[i + 1]
            return previous_char in Language.DIGITS and next_char in Language.DIGITS
        else:
            return False

    def __isTime(self,
                 line: str,
                 i: int) -> bool:
        """
        The isTime method takes a String line and an integer i as inputs. Then, it returns true if
        the result of the contains method, which compares the previous char, next char and two next chars with
        0123456789, returns true and false otherwise.

        PARAMETERS
        ----------
        line : str
            String input to check.
        i : int
            index.

        RETURNS
        -------
        bool
            True if previous char, next char and two next chars are digit, False otherwise.
        """
        if i > 0 and i + 2 < len(line):
            previous_char = line[i - 1]
            next_char = line[i + 1]
            two_next_char = line[i + 2]
            return previous_char in Language.DIGITS and next_char in Language.DIGITS and \
                   two_next_char in Language.DIGITS
        else:
            return False

    def split(self, line: str) -> list:
        """
        The split method takes a String line as an input. Firstly it creates a new sentence as currentSentence a new
        list as sentences. Then loops till the end of the line and checks some conditions;
        If the char at ith index is a separator;

        ' : assigns currentWord as currentWord'
        { : increment the curlyBracketCount
        } : decrement the curlyBracketCount
        " : increment the specialQuotaCount
        " : decrement the specialQuotaCount
        ( : increment roundParenthesisCount
        ) : decrement roundParenthesisCount
        [ : increment bracketCount
        ] : decrement bracketCount
        " : assign quotaCount as 1- quotaCount
        ' : assign apostropheCount as 1- apostropheCount

        If the currentWord is not empty, it adds the currentWord after repeatControl to currentSentence.

        If the char at index i is " and  bracketCount, specialQuotaCount, curlyBracketCount, roundParenthesisCount, and
        quotaCount equal to 0 and also the next char is uppercase or digit, it adds currentSentence to sentences.

        If the char at ith index is a sentence ender;

        . and currentWord is www : assigns webMode as true. Ex: www.google.com
        . and currentWord is a digit or in web or e-mail modes : assigns currentWord as currentWord+char(i) Ex: 1.
        . and currentWord is a shortcut or an abbreviation : assigns currentWord as currentWord+char(i) and adds
        currentWord to currentSentence. Ex : bkz.
        ' and next char is uppercase or digit: add word to currentSentence as ' and add currentSentence to sentences.

        If the char at index i is ' ', i.e space, add word to currentSentence and assign "" to currentSentence.
        If the char at index i is -,  add word to currentSentence and add sentences when the wordCount of
        currentSentence greater than 0.

        If the char at ith index is a punctuation;
        : and if currentWord is "https" : assign webMode as true.
        , and there exists a number before and after : assign currentWord as currentWord+char(i) Ex: 1,2
        : and if line is a time : assign currentWord as currentWord+char(i) Ex: 12:14:24
        - and there exists a number before and after : assign currentWord as currentWord+char(i) Ex: 12-1
        {@literal @} : assign emailMode as true.

        PARAMETERS
        ----------
        line : str
            String input to split.

        RETURNS
        -------
        list
            sentences list which holds split line.
        """
        email_mode = False
        web_mode = False
        i = 0
        special_quota_count = 0
        round_parenthesis_count = 0
        bracket_count = 0
        curly_bracket_count = 0
        quota_count = 0
        apostrophe_count = 0
        current_sentence = Sentence()
        current_word = ""
        sentences = []
        while i < len(line):
            if line[i] in SentenceSplitter.SEPARATORS:
                if line[i] in SentenceSplitter.APOSTROPHES and current_word != "" and self.__isApostrophe(line, i):
                    current_word = current_word + line[i]
                else:
                    if current_word != "":
                        current_sentence.addWord(Word(self.__repeatControl(current_word, web_mode or email_mode)))
                    if line[i] != '\n':
                        current_sentence.addWord(Word("" + line[i]))
                    current_word = ""
                    if line[i] == '{':
                        curly_bracket_count = curly_bracket_count + 1
                    elif line[i] == '}':
                        curly_bracket_count = curly_bracket_count - 1
                    elif line[i] == '\uFF02':
                        special_quota_count = special_quota_count + 1
                    elif line[i] == '\u05F4':
                        special_quota_count = special_quota_count - 1
                    elif line[i] == '“':
                        special_quota_count = special_quota_count + 1
                    elif line[i] == '”':
                        special_quota_count = special_quota_count - 1
                    elif line[i] == '‘':
                        special_quota_count = special_quota_count + 1
                    elif line[i] == '’':
                        special_quota_count = special_quota_count - 1
                    elif line[i] == '(':
                        round_parenthesis_count = round_parenthesis_count + 1
                    elif line[i] == ')':
                        round_parenthesis_count = round_parenthesis_count - 1
                    elif line[i] == '[':
                        bracket_count = bracket_count + 1
                    elif line[i] == ']':
                        bracket_count = bracket_count - 1
                    elif line[i] == '"':
                        quota_count = 1 - quota_count
                    elif line[i] == '\'':
                        apostrophe_count = 1 - apostrophe_count
                    if line[
                        i] == '"' and bracket_count == 0 and special_quota_count == 0 and curly_bracket_count == 0 and \
                            round_parenthesis_count == 0 and quota_count == 0 and self.__isNextCharUpperCaseOrDigit(
                        line,
                        i + 1):
                        sentences.append(current_sentence)
                        current_sentence = Sentence()
            else:
                if line[i] in SentenceSplitter.SENTENCE_ENDERS:
                    if line[i] == '.' and current_word.lower() == "www":
                        web_mode = True
                    if line[i] == '.' and current_word != "" and (
                            web_mode or email_mode or (
                            line[i - 1] in Language.DIGITS and not self.__isNextCharUpperCaseOrDigit(line, i + 1))):
                        current_word = current_word + line[i]
                        current_sentence.addWord(Word(current_word))
                        current_word = ""
                    else:
                        if line[i] == '.' and (
                                self.__listContains(current_word) or self.__isNameShortcut(current_word)):
                            current_word = current_word + line[i]
                            current_sentence.addWord(Word(current_word))
                            current_word = ""
                        else:
                            if line[i] == '.' and self.__numberExistsBeforeAndAfter(line, i):
                                current_word = current_word + line[i]
                            else:
                                if current_word != "":
                                    current_sentence.addWord(
                                        Word(self.__repeatControl(current_word, web_mode or email_mode)))
                                current_word = "" + line[i]
                                i = i + 1
                                while i < len(line) and line[i] in SentenceSplitter.SENTENCE_ENDERS:
                                    i = i + 1
                                i = i - 1
                                current_sentence.addWord(Word(current_word))
                                if round_parenthesis_count == 0 and bracket_count == 0 and curly_bracket_count == 0 and \
                                        quota_count == 0:
                                    if i + 1 < len(line) and line[i + 1] == '\'' and apostrophe_count == 1 and \
                                            self.__isNextCharUpperCaseOrDigit(line, i + 2):
                                        current_sentence.addWord(Word("'"))
                                        i = i + 1
                                        sentences.append(current_sentence)
                                        current_sentence = Sentence()
                                    else:
                                        if i + 2 < len(line) and line[i + 1] == ' ' and line[i + 2] == '\'' and \
                                                apostrophe_count == 1 and self.__isNextCharUpperCaseOrDigit(line,
                                                                                                            i + 3):
                                            current_sentence.addWord(Word("'"))
                                            i += 2
                                            sentences.append(current_sentence)
                                            current_sentence = Sentence()
                                        else:
                                            if self.__isNextCharUpperCaseOrDigit(line, i + 1):
                                                sentences.append(current_sentence)
                                                current_sentence = Sentence()
                                current_word = ""
                else:
                    if line[i] == ' ':
                        email_mode = False
                        web_mode = False
                        if current_word != "":
                            current_sentence.addWord(Word(self.__repeatControl(current_word, web_mode or email_mode)))
                            current_word = ""
                    else:
                        if line[i] == '-' and not web_mode and round_parenthesis_count == 0 and \
                                self.__isNextCharUpperCase(line, i + 1) and \
                                not self.__isPreviousWordUpperCase(line, i - 1):
                            if current_word != "" and current_word not in Language.DIGITS:
                                current_sentence.addWord(
                                    Word(self.__repeatControl(current_word, web_mode or email_mode)))
                            if current_sentence.wordCount() > 0:
                                sentences.append(current_sentence)
                            current_sentence = Sentence()
                            round_parenthesis_count = 0
                            bracket_count = 0
                            curly_bracket_count = 0
                            quota_count = 0
                            special_quota_count = 0
                            if current_word != "" and re.match("\\d+", current_word):
                                current_sentence.addWord(Word(current_word + " -"))
                            else:
                                current_sentence.addWord(Word("-"))
                            current_word = ""
                        else:
                            if line[i] in SentenceSplitter.PUNCTUATION_CHARACTERS or \
                                    line[i] in Language.ARITHMETIC_CHARACTERS:
                                if line[i] == ':' and (current_word == "http" or current_word == "https"):
                                    web_mode = True
                                if web_mode:
                                    current_word = current_word + line[i]
                                else:
                                    if line[i] == ',' and self.__numberExistsBeforeAndAfter(line, i):
                                        current_word = current_word + line[i]
                                    else:
                                        if line[i] == ':' and self.__isTime(line, i):
                                            current_word = current_word + line[i]
                                        else:
                                            if line[i] == '-' and self.__numberExistsBeforeAndAfter(line, i):
                                                current_word = current_word + line[i]
                                            else:
                                                if current_word != "":
                                                    current_sentence.addWord(
                                                        Word(
                                                            self.__repeatControl(current_word, web_mode or email_mode)))
                                                current_sentence.addWord(Word("" + line[i]))
                                                current_word = ""
                            else:
                                if line[i] == '@':
                                    current_word = current_word + line[i]
                                    email_mode = True
                                else:
                                    current_word = current_word + line[i]
            i = i + 1
        if current_word != "":
            current_sentence.addWord(Word(self.__repeatControl(current_word, web_mode or email_mode)))
        if current_sentence.wordCount() > 0:
            sentences.append(current_sentence)
        return sentences

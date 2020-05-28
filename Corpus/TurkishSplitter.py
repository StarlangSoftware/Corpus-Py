from Dictionary.Word import Word
from Language.TurkishLanguage import TurkishLanguage
from Corpus.Sentence import Sentence
from Corpus.SentenceSplitter import SentenceSplitter

import re


class TurkishSplitter(SentenceSplitter):

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
        shortcuts = {"alb", "bnb", "bkz", "bşk", "co", "dr", "dç", "der", "em", "gn",
                     "hz", "kd", "kur", "kuv", "ltd", "md", "mr", "mö", "muh", "müh",
                     "no", "öğr", "op", "opr", "org", "sf", "tuğ", "uzm", "vb", "vd",
                     "yön", "yrb", "yrd", "üniv", "fak", "prof", "dz", "yd", "krm", "gen",
                     "pte", "p", "av", "II", "III", "IV", "VI", "VII", "VIII", "IX",
                     "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
                     "XX", "tuğa", "plt", "tğm", "tic", "srv", "bl", "dipl", "not", "min",
                     "cul", "san", "rzv", "or", "kor", "tüm", "st", "sn", "fr", "pl",
                     "ka", "tk", "ko", "vs", "yard", "bknz", "doç", "gör", "müz", "oyn",
                     "m", "s", "kr", "ms", "hv", "uz", "re", "ph", "mc", "ed",
                     "km", "yb", "bk", "jr", "bn", "os", "mrs", "bld", "sen", "alm",
                     "sir", "ord", "dir", "yay", "man", "brm", "edt", "dec", "mah", "cad",
                     "vol", "kom", "sok", "apt", "elk", "mad", "ort", "cap", "ste", "exc",
                     "ef"}
        return currentWord in shortcuts

    def __isNextCharUpperCaseOrDigit(self, line: str, i: int) -> bool:
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
        if i == len(line) or line[i] in TurkishLanguage.UPPERCASE_LETTERS + TurkishLanguage.DIGITS + "-":
            return True
        else:
            return False

    def __isPreviousWordUpperCase(self, line: str, i: int) -> bool:
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
        while i >= 0 and (line[i] == ' ' or line[i] in TurkishLanguage.LOWERCASE_LETTERS + "qxw"):
            i = i - 1
        if i == -1 or line[i] in TurkishLanguage.UPPERCASE_LETTERS + "QWX":
            return True
        else:
            return False

    def __isNextCharUpperCase(self, line: str, i: int) -> bool:
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
        if i == len(line) or line[i] in TurkishLanguage.UPPERCASE_LETTERS + "\"\'":
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
        if len(currentWord) == 1 and currentWord in TurkishLanguage.UPPERCASE_LETTERS:
            return True
        if len(currentWord) == 3 and currentWord[1] == '.' and currentWord[2] in TurkishLanguage.UPPERCASE_LETTERS:
            return True
        return False

    def __repeatControl(self, word: str, exceptionMode: bool) -> str:
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

    def __isApostrophe(self, line: str, i: int) -> bool:
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
        apostropheLetters = TurkishLanguage.LETTERS + TurkishLanguage.EXTENDED_LANGUAGE_CHARACTERS \
                            + TurkishLanguage.DIGITS
        if i + 1 < len(line):
            previousChar = line[i - 1]
            nextChar = line[i + 1]
            return previousChar in apostropheLetters and nextChar in apostropheLetters
        else:
            return False

    def __numberExistsBeforeAndAfter(self, line: str, i: int) -> bool:
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
        if i + 1 < len(line) and i > 0:
            previousChar = line[i - 1]
            nextChar = line[i + 1]
            return previousChar in TurkishLanguage.DIGITS and nextChar in TurkishLanguage.DIGITS
        else:
            return False

    def __isTime(self, line: str, i: int) -> bool:
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
        if i + 2 < len(line):
            previousChar = line[i - 1]
            nextChar = line[i + 1]
            twoNextChar = line[i + 2]
            return previousChar in TurkishLanguage.DIGITS and nextChar in TurkishLanguage.DIGITS and \
                   twoNextChar in TurkishLanguage.DIGITS
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
        emailMode = False
        webMode = False
        i = 0
        specialQuotaCount = 0
        roundParenthesisCount = 0
        bracketCount = 0
        curlyBracketCount = 0
        quotaCount = 0
        apostropheCount = 0
        currentSentence = Sentence()
        currentWord = ""
        sentences = []
        while i < len(line):
            if line[i] in SentenceSplitter.SEPARATORS:
                if line[i] == '\'' and currentWord != "" and self.__isApostrophe(line, i):
                    currentWord = currentWord + line[i]
                else:
                    if currentWord != "":
                        currentSentence.addWord(Word(self.__repeatControl(currentWord, webMode or emailMode)))
                    currentSentence.addWord(Word("" + line[i]))
                    currentWord = ""
                    if line[i] == '{':
                        curlyBracketCount = curlyBracketCount + 1
                    elif line[i] == '}':
                        curlyBracketCount = curlyBracketCount - 1
                    elif line[i] == '\uFF02':
                        specialQuotaCount = specialQuotaCount + 1
                    elif line[i] == '\u05F4':
                        specialQuotaCount = specialQuotaCount - 1
                    elif line[i] == '(':
                        roundParenthesisCount = roundParenthesisCount + 1
                    elif line[i] == ')':
                        roundParenthesisCount = roundParenthesisCount - 1
                    elif line[i] == '[':
                        bracketCount = bracketCount + 1
                    elif line[i] == ']':
                        bracketCount = bracketCount - 1
                    elif line[i] == '"':
                        quotaCount = 1 - quotaCount
                    elif line[i] == '\'':
                        apostropheCount = 1 - apostropheCount
                    if line[i] == '"' and bracketCount == 0 and specialQuotaCount == 0 and curlyBracketCount == 0 and \
                            roundParenthesisCount == 0 and quotaCount == 0 and self.__isNextCharUpperCaseOrDigit(line,
                                                                                                                 i + 1):
                        sentences.append(currentSentence)
                        currentSentence = Sentence()
            else:
                if line[i] in SentenceSplitter.SENTENCE_ENDERS:
                    if line[i] == '.' and currentWord == "www":
                        webMode = True
                    if line[i] == '.' and currentWord != "" and (
                            webMode or emailMode or line[i - 1] in TurkishLanguage.DIGITS):
                        currentWord = currentWord + line[i]
                    else:
                        if line[i] == '.' and (self.__listContains(currentWord) or self.__isNameShortcut(currentWord)):
                            currentWord = currentWord + line[i]
                            currentSentence.addWord(Word(currentWord))
                            currentWord = ""
                        else:
                            if currentWord != "":
                                currentSentence.addWord(Word(self.__repeatControl(currentWord, webMode or emailMode)))
                            currentWord = "" + line[i]
                            i = i + 1
                            while i < len(line) and line[i] in SentenceSplitter.SENTENCE_ENDERS:
                                i = i + 1
                            i = i - 1
                            currentSentence.addWord(Word(currentWord))
                            if roundParenthesisCount == 0 and bracketCount == 0 and curlyBracketCount == 0 and \
                                    quotaCount == 0:
                                if i + 1 < len(line) and line[i + 1] == '\'' and apostropheCount == 1 and \
                                        self.__isNextCharUpperCaseOrDigit(line, i + 2):
                                    currentSentence.addWord(Word("'"))
                                    i = i + 1
                                    sentences.append(currentSentence)
                                    currentSentence = Sentence()
                                else:
                                    if i + 2 < len(line) and line[i + 1] == ' ' and line[i + 2] == '\'' and \
                                            apostropheCount == 1 and self.__isNextCharUpperCaseOrDigit(line, i + 3):
                                        currentSentence.addWord(Word("'"))
                                        i += 2
                                        sentences.append(currentSentence)
                                        currentSentence = Sentence()
                                    else:
                                        if self.__isNextCharUpperCaseOrDigit(line, i + 1):
                                            sentences.append(currentSentence)
                                            currentSentence = Sentence()
                            currentWord = ""
                else:
                    if line[i] == ' ':
                        emailMode = False
                        webMode = False
                        if currentWord != "":
                            currentSentence.addWord(Word(self.__repeatControl(currentWord, webMode or emailMode)))
                            currentWord = ""
                    else:
                        if line[i] == '-' and not webMode and roundParenthesisCount == 0 and \
                                self.__isNextCharUpperCase(line, i + 1) and \
                                not self.__isPreviousWordUpperCase(line, i - 1):
                            if currentWord != "" and currentWord not in TurkishLanguage.DIGITS:
                                currentSentence.addWord(Word(self.__repeatControl(currentWord, webMode or emailMode)))
                            if currentSentence.wordCount() > 0:
                                sentences.append(currentSentence)
                            currentSentence = Sentence()
                            roundParenthesisCount = 0
                            bracketCount = 0
                            curlyBracketCount = 0
                            quotaCount = 0
                            specialQuotaCount = 0
                            if currentWord != "" and re.match("\\d+", currentWord):
                                currentSentence.addWord(Word(currentWord + " -"))
                            else:
                                currentSentence.addWord(Word("-"))
                            currentWord = ""
                        else:
                            if line[i] in SentenceSplitter.PUNCTUATION_CHARACTERS or \
                                    line[i] in TurkishLanguage.ARITHMETIC_CHARACTERS:
                                if line[i] == ':' and (currentWord == "http" or currentWord == "https"):
                                    webMode = True
                                if webMode:
                                    currentWord = currentWord + line[i]
                                else:
                                    if line[i] == ',' and self.__numberExistsBeforeAndAfter(line, i):
                                        currentWord = currentWord + line[i]
                                    else:
                                        if line[i] == ':' and self.__isTime(line, i):
                                            currentWord = currentWord + line[i]
                                        else:
                                            if line[i] == '-' and self.__numberExistsBeforeAndAfter(line, i):
                                                currentWord = currentWord + line[i]
                                            else:
                                                if currentWord != "":
                                                    currentSentence.addWord(
                                                        Word(self.__repeatControl(currentWord, webMode or emailMode)))
                                                currentSentence.addWord(Word("" + line[i]))
                                                currentWord = ""
                            else:
                                if line[i] == '@':
                                    currentWord = currentWord + line[i]
                                    emailMode = True
                                else:
                                    currentWord = currentWord + line[i]
            i = i + 1
        if currentWord != "":
            currentSentence.addWord(Word(self.__repeatControl(currentWord, webMode or emailMode)))
        if currentSentence.wordCount() > 0:
            sentences.append(currentSentence)
        return sentences

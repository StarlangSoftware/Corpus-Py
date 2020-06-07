from __future__ import annotations
from DataStructure.CounterHashMap import CounterHashMap
from Dictionary.Word import Word

from Corpus.LanguageChecker import LanguageChecker
from Corpus.Paragraph import Paragraph
from Corpus.Sentence import Sentence
from Corpus.SentenceSplitter import SentenceSplitter

import random


class Corpus:

    paragraphs: list
    sentences: list
    wordList: CounterHashMap
    fileName: str

    def __init__(self, fileName=None, splitterOrChecker=None):
        """
        Constructor of Corpus class which takes a file name as an input. Then reads the input file line by line
        and calls addSentence method with each read line.

        PARAMETERS
        ----------
        fileName : str
            String file name input that will be read.
        """
        self.sentences = []
        self.paragraphs = []
        self.wordList = CounterHashMap()
        if fileName is not None:
            self.fileName = fileName
            file = open(fileName, "r", encoding='utf8')
            lines = file.readlines()
            if splitterOrChecker is not None:
                if isinstance(splitterOrChecker, SentenceSplitter):
                    for line in lines:
                        sentences = splitterOrChecker.split(line.strip())
                        paragraph = Paragraph()
                        for sentence in sentences:
                            paragraph.addSentence(sentence)
                        self.addParagraph(paragraph)
                elif isinstance(splitterOrChecker, LanguageChecker):
                    for line in lines:
                        sentence = Sentence(line.strip(), splitterOrChecker)
                        self.addSentence(sentence)
            else:
                for line in lines:
                    self.addSentence(Sentence(line.strip()))

    def combine(self, corpus: Corpus):
        """
        The combine method takes a Corpus as an input and adds each sentence of sentences list.

        PARAMETERS
        ----------
        corpus : Corpus
            Corpus type input.
        """
        for sentence in corpus.sentences:
            self.addSentence(sentence)

    def addSentence(self, s: Sentence):
        """
        The addSentence method takes a Sentence as an input. It adds given input to sentences list and loops
        through the each word in sentence and puts these words into wordList CounterHashMap.

        PARAMETERS
        ----------
        s : Sentence
            Sentence type input that will be added to sentences list and its words will be added to wordList
            CounterHashMap.
        """
        self.sentences.append(s)
        for i in range(s.wordCount()):
            w = s.getWord(i)
            self.wordList.put(w)

    def numberOfWords(self) -> int:
        """
        The numberOfWords method loops through the sentences list and accumulates the number of words in sentence.

        RETURNS
        -------
        int
            size which holds the total number of words.
        """
        size = 0
        for s in self.sentences:
            size += s.wordCount()
        return size

    def contains(self, word: str) -> bool:
        """
        The contains method takes a String word as an input and checks whether wordList CounterHashMap has the
        given word and returns true if so, otherwise returns false.

        PARAMETERS
        ----------
        word : str
            String input to check.

        RETURNS
        -------
        bool
            True if wordList has the given word, False otherwise.
        """
        return Word(word) in self.wordList

    def addParagraph(self, p: Paragraph):
        """
        The addParagraph method takes a Paragraph type input. It gets the sentences in the given paragraph and
        add these to the sentences list and the words in the sentences to the wordList CounterHashMap.

        PARAMETERS
        ----------
        p : Paragraph
            Paragraph type input to add sentences and wordList.
        """
        self.paragraphs.append(p)
        for i in range(p.sentenceCount()):
            self.addSentence(p.getSentence(i))

    def getFileName(self) -> str:
        """
        Getter for the file name.

        RETURNS
        -------
        str
            file name.
        """
        return self.fileName

    def getWordList(self) -> set:
        """
        Getter for the wordList.

        RETURNS
        -------
        set
            The keySet of wordList.
        """
        return set(self.wordList.keys())

    def wordCount(self) -> int:
        """
        The wordCount method returns the size of the wordList CounterHashMap.

        RETURNS
        -------
        int
            The size of the wordList CounterHashMap.
        """
        return len(self.wordList)

    def getCount(self, word: Word) -> int:
        """
        The getCount method returns the count value of given word.

        PARAMETERS
        ----------
        word : Word
            Word type input to check.

        RETURNS
        -------
        int
            The count value of given word.
        """
        return self.wordList[word]

    def sentenceCount(self) -> int:
        """
        The sentenceCount method returns the size of the sentences list.

        RETURNS
        -------
        int
            The size of the sentences list.
        """
        return len(self.sentences)

    def getSentence(self, index: int) -> Sentence:
        """
        Getter for getting a sentence at given index.

        PARAMETERS
        ----------
        index : int
            index to get sentence from.

        RETURNS
        -------
        Sentence
            The sentence at given index.
        """
        return self.sentences[index]

    def paragraphCount(self) -> int:
        """
        The paragraphCount method returns the size of the paragraphs list.

        RETURNS
        -------
        int
            The size of the paragraphs list.
        """
        return len(self.paragraphs)

    def getParagraph(self, index: int) -> Paragraph:
        """
        Getter for getting a paragraph at given index.

        PARAMETERS
        ----------
        index : int
            index to get paragraph from.

        RETURNS
        -------
        Paragraph
            The paragraph at given index.
        """
        return self.paragraphs[index]

    def maxSentenceLength(self) -> int:
        """
        The maxSentenceLength method finds the sentence with the maximum number of words and returns this number.

        RETURNS
        -------
        int
            maximum length.
        """
        maxLength = 0
        for s in self.sentences:
            if s.wordCount() > maxLength:
                maxLength = s.wordCount()
        return maxLength

    def getAllWordsAsList(self) -> list:
        """
        The getAllWordsAsList method creates new list of lists and adds each word in each sentence of sentences
        list into new list.

        RETURNS
        -------
        list
            Newly created and populated list.
        """
        allWords = []
        for i in range(self.sentenceCount()):
            allWords.append(self.getSentence(i).getWords())
        return allWords

    def shuffleSentences(self, seed: int):
        """
        The shuffleSentences method randomly shuffles sentences list with given seed value.

        PARAMETERS
        ----------
        seed : int
            value to randomize shuffling.
        """
        random.seed(seed)
        random.shuffle(self.sentences)

    def getTrainCorpus(self, foldNo: int, foldCount: int) -> Corpus:
        """
        The getTrainCorpus method takes two integer inputs foldNo and foldCount for determining train data size and
        count of fold respectively. Initially creates a new empty Corpus, then finds the sentenceCount as N. Then,
        starting from the index 0 it loops through the index (foldNo * N) / foldCount and add each sentence of sentences
        list to new Corpus. Later on, starting from the index ((foldNo + 1) * N) / foldCount, it loops through the index
        N and add each sentence of sentences list to new Corpus.

        PARAMETERS
        ----------
        foldNo : int
            Integer input for train set size.
        foldCount : int
            Integer input for counting fold.

        RETURNS
        -------
        Corpus
            The newly created and populated Corpus.
        """
        trainCorpus = Corpus()
        N = self.sentenceCount()
        for i in range((foldNo * N) // foldCount):
            trainCorpus.addSentence(self.sentences[i])
        for i in range(((foldNo + 1) * N) // foldCount, N):
            trainCorpus.addSentence(self.sentences[i])
        return trainCorpus

    def getTestCorpus(self, foldNo: int, foldCount: int) -> Corpus:
        """
        The getTestCorpus method takes two integer inputs foldNo and foldCount for determining test data size and count
        of fold respectively. Initially creates a new empty Corpus, then finds the sentenceCount as N. Then, starting
        from the index (foldNo * N) / foldCount it loops through the index ((foldNo + 1) * N) / foldCount and add each
        sentence of sentences list to new Corpus.

        PARAMETERS
        ----------
        foldNo : int
            Integer input for test size.
        foldCount : int
            Integer input counting fold.

        RETURNS
        -------
        Corpus
            The newly created and populated Corpus.
        """
        testCorpus = Corpus()
        N = self.sentenceCount()
        for i in range((foldNo * N) // foldCount, ((foldNo + 1) * N) // foldCount):
            testCorpus.addSentence(self.sentences[i])
        return testCorpus

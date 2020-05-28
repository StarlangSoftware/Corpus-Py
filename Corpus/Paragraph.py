from Corpus.Sentence import Sentence


class Paragraph:

    __sentences: list

    def __init__(self):
        """
        A constructor of Paragraph class which creates a list sentences.
        """
        self.__sentences = []

    def addSentence(self, s: Sentence):
        """
        The addSentence method adds given sentence to sentences list.

        PARAMETERS
        ----------
        s : Sentence
            Sentence type input to add sentences.
        """
        self.__sentences.append(s)

    def sentenceCount(self) -> int:
        """
        The sentenceCount method finds the size of the list sentences.

        RETURNS
        -------
        int
            The size of the list sentences.
        """
        return len(self.__sentences)

    def getSentence(self, index: int) -> Sentence:
        """
        The getSentence method finds the sentence from sentences list at given index.

        PARAMETERS
        ----------
        index : int
            used to get a sentence.

        RETURNS
        -------
        Sentence
            sentence at given index.
        """
        return self.__sentences[index]

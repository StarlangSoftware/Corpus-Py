from enum import Enum, auto


class WordFormat(Enum):

    """
    Surface/Original form
    """
    SURFACE = auto()
    """
    Create 2-Gram words as output.
    """
    LETTER_2 = auto()
    """
    Create 3-Gram words as output.
    """
    LETTER_3 = auto()
    """
    Create 4-Gram words as output.
    """
    LETTER_4 = auto()

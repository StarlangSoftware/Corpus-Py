import unittest

from Corpus.TurkishSplitter import TurkishSplitter


class TurkishSplitterTest(unittest.TestCase):

    splitter: TurkishSplitter

    def setUp(self) -> None:
        self.splitter = TurkishSplitter()

    def test_Split(self):
        self.assertEqual(14, len(self.splitter.split("Cin Ali, bak! " +
                "At. " +
                "Bak, Cin Ali, bak. " +
                "Bu at. " +
                "Baba, o atı bana al. " +
                "Cin Ali, bu at. " +
                "O da ot. " +
                "Baba, bu ata ot al. " +
                "Cin Ali, bu ot, o da at. " +
                "Otu al, ata ver. " +
                "Bak, Suna! " +
                "Cin Ali, ata ot verdi. " +
                "Su verdi. " +
                "Cin Ali, ata bir kova da su verdi.")))


if __name__ == '__main__':
    unittest.main()

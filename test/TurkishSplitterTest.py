import unittest

from Corpus.TurkishSplitter import TurkishSplitter


class TurkishSplitterTest(unittest.TestCase):

    splitter: TurkishSplitter

    def setUp(self) -> None:
        self.splitter = TurkishSplitter()

    def test_Split1(self):
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

    def test_Split2(self):
        self.assertEqual(1, len(self.splitter.split("WWW.GOOGLE.COM")))

    def test_Split3(self):
        self.assertEqual(1, len(self.splitter.split("www.google.com")))

    def test_Split4(self):
        self.assertEqual(1, len(self.splitter.split("1.adımda ve 2.adımda ne yaptın")))
        self.assertEqual(7, self.splitter.split("1.adımda ve 2.adımda ne yaptın")[0].wordCount())

    def test_Split5(self):
        self.assertEqual(1, len(self.splitter.split("1. adımda ve 2. adımda ne yaptın")))
        self.assertEqual(7, self.splitter.split("1. adımda ve 2. adımda ne yaptın")[0].wordCount())

    def test_Split6(self):
        self.assertEqual(1, len(self.splitter.split("Burada II. Murat ve I. Ahmet oyun oynadı")))
        self.assertEqual(8, self.splitter.split("Burada II. Murat ve I. Ahmet oyun oynadı")[0].wordCount())

    def test_Split7(self):
        self.assertEqual(1, len(self.splitter.split("1.87 cm boyunda ve 84 kg ağırlığındaydı")))
        self.assertEqual(7, self.splitter.split("1.87 cm boyunda ve 84 kg ağırlığındaydı")[0].wordCount())

    def test_Split8(self):
        self.assertEqual("AAA", self.splitter.split("AA piller, AAA pillerin yaklaşık üç kat kapasitesine sahiptir")[0].getWord(3).getName())
        self.assertEqual("yakala", self.splitter.split("Topu atıp yakalaaaa diye bağırdı")[0].getWord(2).getName())

    def test_Split9(self):
        self.assertEqual(1, len(self.splitter.split("Bunun yanı sıra erkek t-shirt modellerini klasik giyim tarzına uyarlayarak kullanmak da mümkündür")))
        self.assertEqual(13, self.splitter.split("Bunun yanı sıra erkek t-shirt modellerini klasik giyim tarzına uyarlayarak kullanmak da mümkündür")[0].wordCount())
        self.assertEqual(1, len(self.splitter.split("USB-C, USB-A’ya göre çok daha yüksek hızlarda aktarım sağlayabilir")))
        self.assertEqual(10, self.splitter.split("USB-C, USB-A’ya göre çok daha yüksek hızlarda aktarım sağlayabilir")[0].wordCount())

if __name__ == '__main__':
    unittest.main()

# Corpus

Nlptoolkit’in birimlendirici/cümle bölücü bileşeni, bir serbest metnin birimlerini ve/veya cümlelerini saptamak için kullanılabilir. Bu bileşen, kural tabanlı bir bileşen olup girdiyi önceden belirlenmiş bir kural kümesini takip ederek cümlelere ve birimlerine ayırır. Bu kural kümesi, bir sonraki karakterin küçük/büyük harf olması gibi cümle düzeyinde kurallar içerdiği gibi, bir girdinin Türkçe’deki yaygın kısaltmalar arasında olup olmadığını kontrol etmek gibi dil düzeyinde kurallar da içerir. Özetle, birimlendirici/cümle bölücü bileşeni bir girdi olarak serbest metin alır ve çıktı olarak birimlerine ayrılmış bir cümle kümesi verir.

For Developers
============
You can also see [Java](https://github.com/starlangsoftware/Corpus), [C++](https://github.com/starlangsoftware/Corpus-CPP), or [C#](https://github.com/starlangsoftware/Corpus-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called EnglishPosTagger will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/Corpus-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `Corpus-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============
+ [Corpus](#corpus)
+ [TurkishSplitter](#turkishsplitter)

## Corpus

Bir derlemi hafızaya atmak için

	a = Corpus("derlem.txt")

Bu derlem eğer noktalarla bölünmüş fakat cümlelere bölünmemiş ise

	Corpus(self, fileName=None, splitterOrChecker=None)

Derlemdeki cümle sayısı

	sentenceCount(self) -> int

Derlemdeki i. cümle ise

	getSentence(self, index: int) -> Sentence

## TurkishSplitter

Türkçe . kurallarına göre cümlelere ayırmak için TurkishSplitter sınıfı kullanılır.

	split(self, line: str) -> list

Corpus
============

Video Lectures
============

[<img src="https://github.com/StarlangSoftware/Corpus/blob/master/video.jpg" width="50%">](https://youtu.be/xTrdKY5uI08)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/Corpus-Cy), [Java](https://github.com/starlangsoftware/Corpus), [C++](https://github.com/starlangsoftware/Corpus-CPP), [Swift](https://github.com/starlangsoftware/Corpus-Swift), [Js](https://github.com/starlangsoftware/Corpus-Js), or [C#](https://github.com/starlangsoftware/Corpus-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-Corpus

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Corpus will be created. Or you can use below link for exploring the code:

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

To store a corpus in memory

	a = Corpus("derlem.txt")

If this corpus is split with dots but not in sentences

	Corpus(self, fileName=None, splitterOrChecker=None)

The number of sentences in the corpus

	sentenceCount(self) -> int

To get ith sentence in the corpus

	getSentence(self, index: int) -> Sentence

## TurkishSplitter

TurkishSplitter class is used to split the text into sentences in accordance with the . rules of Turkish.

	split(self, line: str) -> list

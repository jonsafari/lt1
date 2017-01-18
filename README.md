# Language Technology I
## A Graduate Course

<br>

## Info
Instructors: Dr. [Jon Dehdari](http://jon.dehdari.org) and Dr. [Asad Sayeed](http://www.coli.uni-saarland.de/~asayeed) <br>
Class Location: (Former) CiP Room, building C7.2 <br>
Class Times: Lecture: Mondays **14**:00-16:00 ([c.t](https://en.wikipedia.org/wiki/Academic_quarter_(class_timing))); Lab: Wednesdays **16**:00-18:00 ([s.t](https://en.wikipedia.org/wiki/Academic_quarter_(class_timing))) <br>
Class Dates: Oct. 31st - Feb. 15th <br>
Jon's Offices: either room 1.15, building A2.2, or room 1.11 building D3.1 <br>
Asad's Office: room 3.04, building C7.4


## Purpose
Language Technologies I teaches the theoretical foundation of modern computational linguistics and natural language processing.
This includes important machine learning techniques.


## Outline
1. [Formal models of language: possibilities](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/formal_models_of_language.pdf) ([homework](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/Exercise-1.pdf))
2. [Statistical models of language: probabilities](https://drive.google.com/open?id=0B-aFax-9-qt3OU1tMmJFSF85Nnc) ([homework](hw/probs.md))
3. [Applications of language models](https://drive.google.com/open?id=0B-aFax-9-qt3b3dnSHJkSGlHaVU)
4. [*n*-gram language models and smoothing](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/ngram_smooth.pdf) ([more info](http://www.statmt.org/book/slides/07-language-models.pdf)) ([homework](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/Exercise-4.pdf)) ([training data](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/Exercise-4-Training.txt)) ([testing data](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/Exercise-4-Testing.txt)) ([example transcript](examples/Week4.ipynb)) ([Bad-Turing transcript](examples/Bad-Turing.ipynb)) ([lazy tokenization script](examples/tokcorpus.py))
5. [Parts of speech, word clusters, and class-based language models](https://drive.google.com/open?id=0B-aFax-9-qt3X1B5UVVUZUZxUDQ)
6. [Log-linear models](https://drive.google.com/open?id=0B-aFax-9-qt3ZUdrU2VzeGU0YzA) ([homework](https://drive.google.com/open?id=0B-aFax-9-qt3X2lwdFZYY2NGOE0))
7. [Word vectors, and applications](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/word_vectors.pdf) ([homework](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/Exercise-7.pdf))
8. [Feedforward neural networks and autoencoders](https://drive.google.com/open?id=0B-aFax-9-qt3SW5GUGtyUk91a1k) ([homework](hw/hw-ffnn.md))
9. [Recurrent neural networks and their language models](http://www.coli.uni-saarland.de/~asayeed/LT1-WS1617/nnets_2.pdf) ([homework](hw/hw-rnn.md))
10. [Probabilistic context-free grammars, parsing, and syntactic language models](https://drive.google.com/open?id=0B-aFax-9-qt3YXVITS1ZNGhzX3M)
11. [Sequence-to-sequence models and neural machine translation](https://drive.google.com/open?id=0B-aFax-9-qt3SENHNFpCTGh3U1k)
12. [Convolutional networks and character-based models of language](https://drive.google.com/open?id=0B-aFax-9-qt3VGhTb01ERGxvUkk)

## External Links
- Neural Network Software:
 - [Keras](http://keras.io), an easy neural network library.  You can install it by typing the following from the command line:

       pip install --user keras

 - [List of other software for neural networks](http://deeplearning.net/software_links)
 - [Another list of recurrent neural network stuff](https://github.com/kjw0612/awesome-rnn)
- Free Corpora:
 - [WMT Data](http://www.statmt.org/wmt16/translation-task.html#download), both parallel and monolingual corpora
 - [ACL Wiki, "Resources by Language"](http://aclweb.org/aclwiki/index.php?title=List_of_resources_by_language)
 - [OPUS - open parallel corpora](http://opus.lingfil.uu.se)
- Corpus Processing Tools:
 - https://github.com/jonsafari/habeas-corpus
 - https://github.com/kpu/preprocess
 - http://corpus.tools

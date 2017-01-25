# LT1 Homework: CFGs with probabilities

Please email your solution to langtech1saarlandws1617@gmail.com with the subject header **Exercise PCFG**, by **15:00, February 1, 2017**.  Use the email address only for solutions, address questions directly to Asad (asayeed@coli.uni-saarland.de).  Please no Word documents or Zip files. Just good clean Python files, text files, PDFs, and the body text of your email.

In this exercise, we'll look at context-free grammars with probabilities by parsing text, and learn a little bit more about common toolchains like the Stanford Parser, and reverse-engineer the parser a little bit.

1. Download the text file containing Charles Dickens' ["A Tale of two Cities"](http://www.gutenberg.org/files/98/98-0.txt). This is our "training corpus."

2. Strip off Project Gutenberg's preamble and "postamble" from the training corpus
and apply any sentence tokenisation (e.g. Punkt) that you used in a previous assignment, so that there is one sentence per line.

3. For each sentence in the corpus, run the [Stanford Parser](http://nlp.stanford.edu/software/lex-parser.shtml) and collect the constituency parses.  You can do that either inside NLTK/Python or outside via Java.
 * [Some instructions](https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software) on installing the Stanford Parser so that you can use it in NLTK.
 * The [parsing API](http://www.nltk.org/api/nltk.parse.html) under NLTK. Look for the nltk.parse.stanford
 * You may need to adjust the memory options.  If this turns out to be a problem, we will talk about this in class.  It's relatively simple.

4. Construct a probabilistic grammar in the following way (in Python). For each constituency-parsed sentence, if X is a non-terminal and Y1...Yn is its children, add a rule X -> Y1...Yn to the grammar, if it is not already part of the grammar. Keep a count of each time you meet a rule.  Also keep terminal rules like X -> word.

5. Use maximum likelihood estimation on a per-terminal basis to find the probability of each rule in the grammar.

6. 85% of your grade will consist of the following:
 * A Python script containing at least the grammar-construction (from the Stanford parses) and probability calculation
 * A text file containing human-readable rules with probabilities, ideally sorted by non-terminal with the single-word terminal rules at the end.

7. Run the Stanford parser on the following sentences from Emily Brontë's ["Wuthering Heights"](http://www.gutenberg.org/cache/epub/768/pg768.txt), after applying the same sentence tokenization:
 * "Meanwhile, the young man had slung on to his person a decidedly shabby upper garment, and, erecting himself before the blaze, looked down on me from the corner of his eyes, for all the world as if there were some mortal feud unavenged between us.  I began to doubt whether he were a servant or not: his dress and speech were both rude, entirely devoid of the superiority observable in Mr. and Mrs. Heathcliff; his thick brown curls were rough and uncultivated, his whiskers encroached bearishly over his cheeks, and his hands were embrowned like those of a common labourer: still his bearing was free, almost haughty, and he showed none of a domestic's assiduity in attending on the lady of the house.  In the absence of clear proofs of his condition, I deemed it best to abstain from noticing his curious conduct; and, five minutes afterwards, the entrance of Heathcliff relieved me, in some measure, from my uncomfortable state."

8. Ignoring terminals (ie, words), calculate the log-probability of each sentence relative to the probabilistic grammar you built from the Dickens novel, given the trees you obtained for each of them. As the grammar is unsmoothed, the probability or some of them could be zero.

9. For 15% of your grade on this assignment, provide:
 * The log probability of each of the sentences.
 * For the ones that failed with zero probability on the Dickens grammar, give the production that was missing from the grammar to give it zero probability.


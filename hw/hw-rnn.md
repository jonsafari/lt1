# LT1 Homework: Recurrent Neural Networks

Please email your solution to langtech1saarlandws1617@gmail.com with the subject header **Exercise RNN**, by **15:00, January 25, 2016**.  Please no Word documents or Zip files. Just good clean Python files, text files, PDFs, and the body text of your email.

In this exercise, we'll create Twitter bots! (And unleash on the world a small army of students who know how to make bots :D )

1. Find and download any coherent text of your choosing of about
half a million words or more (ideally, more).  You can use Project Gutenberg, crawl the web to build a corpus, or what have you.  

2. Follow the steps in the first part of [this web page](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library), specifically the part about "Twitterbot that Tweets from a File". The instructions are intended for Linux, should work similarly on a Mac too, we can't really help you if you are on Windows (sorry). Pick a relevant name for your bot based on the text, but end the username with "Bot".

3. Use Keras on whatever version of Python to train a 140-character text generator on your corpus.  Specifically, use RNN, LSTM, or GRU to make either a character- or word-based tweet generator from that text (you can use a smaller corpus for a character-based model if it's too slow to train).  It should permit variable-length tweets.   

4. Connect the bot to the neural network you trained.  Unleash the bot on Twitter.  Let it tweet once every 10 minutes for 5 hours.

5. Submit the following:
 * The Python code you wrote as an attachment or as a link to a GitHub repo.
 * A short report (few paragraphs) describing the structure of the model you built as well as the parameters you used.  Tell us if you used a character or word-based model, which type of recurrent structure you used, the number of hidden layers, size of the layers, the length of sequences, and so on.  Also talk about your data source.  Describe any experiments you may have done in the course of development.
 * Since this is a language model, include a graph of the perplexity of the model over 10 training epochs.

6. Because training takes time, we recommend starting this early, just so that you have time to train a nice model.  
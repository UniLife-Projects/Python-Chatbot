# Hudson's Drip™ customer service AI Chatbot

We created an Artificial-intelligence powered chatbot to serve the customers of our online clothing store: Hudson's Drip. We used an agile SDLC methodology, with our development cycle consisting of two scrums.

Our software consists of two input JSON files used to train the neural network and make personalized answers based on customer information. The training.py imports data from intents.py and trains the neural network. training.py outputs words and classes pk1 files, which are used by the predict.py module to estimate the probability that a user input addresses a particular topic in the intents.JSON. A random response from the most likely topic is outputted by the chatbot. Our bot is also able to empathize with the user and take into account the mood of the user when generating responses.

Several libraries were used: tkntr, random, json, pickle, numpy, nltk (Porterstemmer, word net lemmatizer, Sentiment intensity analyzer), and tensorflow.

[JIRA Roadmap](https://durvan.atlassian.net/jira/software/projects/CT3/boards/).  
[Reference material](https://www.youtube.com/watch?v=1lwddP0KUEg).

## COSC 310 Group members:

- Guiherme Durvan António Zandamela
- Lakshay Karnwal
- Abdulaziz Almutlaq
- Ravil Bigvava
- Jordan onwuvuche

### Assignment 3 tasks:

#### GUI Implementation

![GUI Screenshot](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/botdemo.png)

The GUI was implemented using the Python tkinter module for graphical interfaces. Using this module we created a text box where the user enters their query/text. This helps the app become intuitivey easy-to-use for the user.

#### Test cases implementation

The Automated Unit Testing Framework used for this was pytest due to its easy to use module functions. We created multiple test cases for all the important functions which checks if all the functions are working as desired. You can run the Unit testing file using the pytest command. After running the test file, pytest displays a summary of failed and passed functions. If the functions do not pass that means the chatbot will have errors, if all the functions pass that means the program is working as desired.

![Unit Testing Screenshot](https://user-images.githubusercontent.com/60047109/159101549-550633ec-41f7-408e-8fa5-5a43b64d2d75.png)

In the screenshot example above, one of the functions failed because the value of probability was not correct. This is a useful feature as it reduces effort to debug the code.

#### Sentiment analysis

We used a natural language toolkit "Sentiment intensity analyzer" to obtain positivity and negativity scores from the words in the user input. This information was used to make conditional statements in which the response of the bot is either complemented or replaced (depending on the intensity) by a response designed to address the sentiment of the user.

![Sentiment analysis demo](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/sentimentdemo.png)

#### Word stemming in ambiguous cases

Word stemming was used in addition to unstemmed input. Our algorithm stems the user input if the bot is not able to find a probable intent (probability > 0.50).
This helps to prevent inaccurate responses and can address suffixes.

![Sentiment analysis demo](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/sentimentdemo.png)

## API Integration

The APIs integrated utilise the already existent bot that was submitted in assignments prior to this
More information has been added to the intents such that the bot can utilise the API's that are integrated

#### API's Integrated

- **Wikipedia API**

  > Extracts useful knowledge such as definitions, history and so much more that may be relevant to the conversation wit the user.
  > ![Wikipedia Logo](https://pngimg.com/uploads/wikipedia/wikipedia_PNG10.png)

- **Flickr API**
  > Enables the user to search specific tags based on one's conversation and hereafter returns relevant results.
  > ![Flickr Logo](https://www.medfieldpubliclibrary.org/wp-content/uploads/2018/05/flickr-logo.png)

### API Usage

- [x] Clone the repository
- [ ] Install [tensorflow](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-mac-metal-jul-2021.ipynb)
- [ ] Install [Anaconda](https://www.anaconda.com/products/distribution)
- [ ] Install [VSCode](https://code.visualstudio.com/download)
- [ ] Install any other packages as advised in terminal

#### Getting Started

The 'wikiAPI' class gets you connected to the Wikipedia API from your laptop. You can communicate with the bot and retrieve articles, items reviews and even list nearby places

The 'theFlickrApi' class gets you connected to the Flickr API from your computer. This will enable you to retrieve images from Flickr loaded onto your computer depending on how you interact with the bot.

#### Installation

> To install the Flickr API into a virtualenv, run::

```python
pip install --user poetry
poetry install
```

> To install the latest version of Flickr from PyPi:

```python
pip install flickrapi
```

> To install the Wikipedia Kit to your Xcode Project:
> [Use the Swift Package Manager](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)

> To install the WikipediaKit:
> Use [Carthage](https://github.com/Carthage/Carthage)

#### Languages Used

> The bot works with the English language

#### Example of Bot Usage

> User enters: "Show me shoes"
> Bot: Loads shoes from Flickr

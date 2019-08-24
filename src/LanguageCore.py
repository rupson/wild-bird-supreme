# Language base for Consuela

import random

NOUN_SOURCE = "nounlist.txt"
VERB_SOURCE = "language-files/verbs/31Kverbs.txt"
NAME_SOURCE = "language-files/names/yob2018.txt"


def getWordsFromFile(sourcePath):
    words = []
    wordsFile = open(sourcePath, "r")
    for line in wordsFile:
        if line != '':
            words.append(line.strip())
    wordsFile.close()
    return words


def _getWordsFromFile():
    words = []
    wordsFile = open("nounlist.txt", "r")
    for line in wordsFile:
        if line != '':
            words.append(line.strip())
    wordsFile.close()
    return words


def getRandomNameFromFile(sourcePath):
    words = []
    wordsFile = open(sourcePath, "r")
    for line in wordsFile:
        if line != '':
            words.append(line.strip().split(",")[0])
    wordsFile.close()
    return words[random.randint(0, len(words))]


def make_status(name, nouns, verbs):
    status = "{0} {1} {2}. xoxo".format(name, verbs[random.randint(0, len(verbs))], nouns[random.randint(
        0, len(nouns))])
    return status


def make_noun_status(words, STATUS_LENGTH):
    status = words[random.randint(0, len(words))].title()
    for i in range(STATUS_LENGTH - 1):
        status = "{0} {1}".format(status, words[random.randint(0, len(words))])
    status = "{0}. xoxo".format(status)
    return status


def compose_noun_tweet():
    STATUS_LENGTH = 5
    words = _getWordsFromFile()
    return make_noun_status(words, STATUS_LENGTH)


def compose_tweet():
    STATUS_LENGTH = 5
    nounsList = getWordsFromFile(NOUN_SOURCE)
    verbsList = getWordsFromFile(VERB_SOURCE)
    name = getRandomNameFromFile(NAME_SOURCE)
    return make_status(name, nounsList, verbsList)

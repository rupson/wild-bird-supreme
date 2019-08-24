# Language base for Consuela

import random


def getWordsFromFile():
    words = []
    wordsFile = open("nounlist.txt", "r")
    for line in wordsFile:
        if line != '':
            words.append(line.strip())
    wordsFile.close()
    return words


def make_status(words, STATUS_LENGTH):
    status = words[random.randint(0, len(words))].title()
    for i in range(STATUS_LENGTH - 1):
        status = "{0} {1}".format(status, words[random.randint(0, len(words))])
    status = "{0}. xoxo".format(status)
    return status


def compose_tweet():
    STATUS_LENGTH = 5
    words = getWordsFromFile()
    return make_status(words, STATUS_LENGTH)

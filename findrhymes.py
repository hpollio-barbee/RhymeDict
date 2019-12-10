import nltk
import nltk.corpus


def findrhyme(phones):
    for i in phones:
        if phones[-i][-1] in '12':
            return phones[-i:]

entries = nltk.corpus.cmudict.entries()
rhymedict = {}
for word, pron in entries:
    rhyme = (findrhyme(pron),)
    if rhyme in rhymedict:
        rhymedict[rhyme].add(word)
    else:
        rhymedict[rhyme] = {word}

def searchrhyme(word):
    if word in rhymedict.keys():
        wrdrhyme = findrhyme(nltk.corpus.cmudict.dict[word])
        rhymelist = rhymedict[wrdrhyme] - word
        print(word + " rhymes with:\n")
        print(str(i) for i in rhymelist)
    else:
        print(word + " is not in the dictionary. Sorry!")

if __name__ == "__main__":
    searchrhyme('fire')
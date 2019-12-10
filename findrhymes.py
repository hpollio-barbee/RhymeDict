import nltk
import nltk.corpus


def findrhyme(phones):
    for i in range(len(phones)):
        if len(phones[-i]) == 3:
            if phones[-i][2] in '12':
                return tuple(phones[-i:])

entries = nltk.corpus.cmudict.entries()
rhymedict = {}
for (word, pron) in entries:
    rhyme = findrhyme(pron)
    if rhyme in rhymedict:
        rhymedict[rhyme].append(word)
    else:
        rhymedict[rhyme] = [word]

def searchrhyme(word):
    if word in nltk.corpus.cmudict.words():
        phones = nltk.corpus.cmudict.dict()[word][0]
        wrdrhyme = findrhyme(phones)
        rhymelist = rhymedict[wrdrhyme]
        print(word + " rhymes with:\n")
        print(rhymelist)
    else:
        print(word + " is not in the dictionary. Sorry!")

if __name__ == "__main__":
    print(searchrhyme('string'))
    print(searchrhyme('illusion'))
    print(searchrhyme('slandering'))
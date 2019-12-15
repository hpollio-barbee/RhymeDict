import nltk
import nltk.corpus


def findrhyme(phones):
    for i in range(len(phones)):
        if len(phones[-i]) == 3:  # checks to see if the phone is 3 characters long (only vowels are 3 long)
            if phones[-i][2] in '12':  # checks to see if the vowel is either primary or secondary stress
                return tuple(phones[-i:])  # returns the phones of the word from the stressed vowel to the end


entries = nltk.corpus.cmudict.entries()
rhymedict = {}
for (wrd, pron) in entries:
    rhyme = findrhyme(pron)  # gets the rhyme of the word in an entry in the CMUdict
    if rhyme in rhymedict:
        rhymedict[rhyme].append(wrd)  # adds a new value to the key (rhyme) if the key exists
    else:
        rhymedict[rhyme] = [wrd]  # adds a new key and initial value if the key doesn't exist


def subseqrhyme(word):
    phones = nltk.corpus.cmudict.dict()[word][0]
    wrdrhyme = findrhyme(phones)
    list(wrdrhyme)
    subrhymes = tuple(wrdrhyme.append('S'))  # adds the [s] to the end of the rhyme
    subrhymet = tuple(wrdrhyme.append('T'))  # adds the [t] to the end of the rhyme
    subrhymez = tuple(wrdrhyme.append('Z'))  # adds the [z] to the end of the rhyme
    subrhymed = tuple(wrdrhyme.append('D'))  # adds the [d] to the end of the rhyme
    # adds all of the lists of subsequence rhymes together to form one giant list
    rhymelist = rhymedict[subrhymes] + rhymedict[subrhymet] + rhymedict[subrhymez] + rhymedict[subrhymed]
    print(word + " subsequence rhymes with:\n")
    print(rhymelist)


def searchrhyme(word):
    if word in nltk.corpus.cmudict.words():
        phones = nltk.corpus.cmudict.dict()[word][0]  # gets the phones from the entry in the dictionary
        wrdrhyme = findrhyme(phones)  # finds the rhyme in the phones
        rhymelist = rhymedict[wrdrhyme]  # creates a list of all the values at the rhymedict key that matches wrdrhyme
        print(word + " rhymes with:\n")
        print(rhymelist)
        subseqrhyme(word)
    else:
        print(word + " is not in the dictionary. Sorry!")


if __name__ == "__main__":
    print(searchrhyme('string'))
    print(searchrhyme('illusion'))
    print(searchrhyme('slandering'))
import nltk
import nltk.corpus
import itertools as it
import ast

# finds the part of the word that makes it "rhyme"
def findrhyme(phones):
    for i in range(len(phones)):
        if len(phones[-i]) == 3:  # checks to see if the phone is 3 characters long (only vowels are 3 long)
            if phones[-i][2] in '12':  # checks to see if the vowel is either primary or secondary stress
                return tuple(phones[-i:])  # returns the phones of the word from the stressed vowel to the end


entries = nltk.corpus.cmudict.entries()

# all vowels with no stress for featural rhymes
vowels0 = {'AA0', 'AE0', 'AH0', 'AO0', 'AW0', 'AY0', 'EH0', 'ER0', 'EY0', 'IH0', 'IY0', 'OW0', 'OY0', 'UH0', 'UW0'}
# all vowels with primary stress for featural rhymes
vowels1 = {'AA1', 'AE1', 'AH1', 'AO1', 'AW1', 'AY1', 'EH1', 'ER1', 'EY1', 'IH1', 'IY1', 'OW1', 'OY1', 'UH1', 'UW1'}
# all vowels with secondary stess  for featural rhymes
vowels2 = {'AA2', 'AE2', 'AH2', 'AO2', 'AW2', 'AY2', 'EH2', 'ER2', 'EY2', 'IH2', 'IY2', 'OW2', 'OY2', 'UH2', 'UW2'}

vowels = vowels0.union(vowels1, vowels2)

# dictionary containing every consonant as a key with the entry being the two closest phones to the key
ranking = {'B': ['P', 'D'], 'CH': ['SH', 'JH'], 'D': ['T', 'JH'], 'DH': ['TH', 'V'],
           'F': ['V', 'TH'], 'G': ['K', 'D'], 'JH': ['ZH', 'CH'], 'K': ['G', 'T'], 'L': ['R'],
           'M': ['N', 'NG'], 'N': ['NG', 'M'], 'NG': ['N', 'M'], 'P': ['B', 'T'], 'R': ['L'],
           'S': ['Z', 'T'], 'SH': ['ZH', 'CH'], 'T': ['D', 'CH'], 'TH': ['DH', 'F'],
           'V': ['F', 'DH'], 'Z': ['S', 'ZH'], 'ZH': ['JH', 'SH']}

rhymedict = {}

for (wrd, pron) in entries:
    rhyme = findrhyme(pron)  # gets the rhyme of the word in an entry in the CMUdict
    if rhyme in rhymedict:
        rhymedict[rhyme].append(wrd)  # adds a new value to the key (rhyme) if the key exists
    else:
        rhymedict[rhyme] = [wrd]  # adds a new key and initial value if the key doesn't exist


def converttohash(rhyme, X):  # makes it easier to create new entries for rhyme dictionary
    rhyme = rhyme.copy()
    rhyme.append(X)
    rhyme = tuple(rhyme)
    return rhyme


# function to find subsequence rhymes
def subseqrhyme(word):
    if word in nltk.corpus.cmudict.words():
        phones = nltk.corpus.cmudict.dict()[word][0]
        wrdrhyme = list(findrhyme(phones))
        subrhymes = converttohash(wrdrhyme, 'S')  # creates rhyme with S added to the end
        subrhymet = converttohash(wrdrhyme, 'T')  # creates rhyme with T added to the end
        subrhymez = converttohash(wrdrhyme, 'Z')  # creates rhyme with Z added to the end
        subrhymed = converttohash(wrdrhyme, 'D')  # creates rhyme with D added to the end
        entrylist = [subrhymes, subrhymet, subrhymez, subrhymed]
        # adds all of the lists of subsequence rhymes together to form one giant list
        rhymelist = []
        for entry in entrylist:
            if entry in rhymedict:
                rhymelist.append(rhymedict[entry])
        return rhymelist


# class responsible for getting all featural rhymes from rhyme
class FeatureRhyme:
    def __init__(self, rnkng , rhm, rhmdict):
        self.rnkng = rnkng  # field to bring in consonant feature ranking dict; format: dictionary w/ list entries
        self.rhm = rhm  # the original rhyme of the word; format: tuple
        self.rhymes = list(rhm)  # list that will have all of the featural rhyme keys; format: list
        self.rhmdict = rhmdict  # the entire rhyme dictionary

    # generates a dictionary with all the features in the
    def genfeaturerhymes(self):
        rhymesdict = {}
        cartesianlist = []
        for i in range(0, len(self.rhm)):
            if self.rhm[i] not in vowels:  # self.rhm[i] type: String
                rhymesdict[i] = self.rnkng[self.rhm[i]]  # adds the value of the rnkng dict if it's a consonant
                cartesianlist.append(rhymesdict[i])
            else:
                vowelpass = self.rhm[i].split(" ")  # creats a list out of the entire string for the phone
                rhymesdict[i] = vowelpass  # just adds the vowel string if it's a vowel
                cartesianlist.append(rhymesdict[i])
        return list(it.product(*cartesianlist))

    def getrhymes(self, combinations):
        rhymelist = []
        for entry in combinations:
            if entry in rhymedict:
                rhymelist.append(rhymedict[entry])
        return rhymelist



def searchrhyme(word):
    if word in nltk.corpus.cmudict.words():
        phones = nltk.corpus.cmudict.dict()[word][0]  # gets the phones from the entry in the dictionary
        wrdrhyme = findrhyme(phones)  # finds the rhyme in the phones
        rhymelist = rhymedict[wrdrhyme]  # creates a list of all the values at the rhymedict key that matches wrdrhyme
        fr = FeatureRhyme(ranking, wrdrhyme, rhymedict)
        allrhymes = fr.genfeaturerhymes()
        print(word + " rhymes with:\n")
        print(rhymelist)
        print("\n" + word + " subsequence rhymes with:\n")
        print(subseqrhyme(word))
        print("\n" + word + " featural rhymes with:\n")
        if len(fr.getrhymes(allrhymes)) == 0:
            print(word + " has no featural rhymes")
        else:
            print(fr.getrhymes(allrhymes))
    else:
        print(word + " is not in the dictionary. Sorry!")


if __name__ == "__main__":
    rhymequery = input("Please enter a word to rhyme: ")
    print(searchrhyme(rhymequery))

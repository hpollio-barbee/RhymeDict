# RhymeDict
Rhyming Dictionary based on the CMU Pronunciation dictionary that finds perfect rhymes, subsequence rhymes, and featural rhymes. Currently, the features are as follows:

# Perfect Rhymes
This feature compares an input word with other words in the CMU corpus starting at the last stessed vowel.

# Subsequence Rhymes
This feature adds common inflectional phones to the ends of rhymes and searches for perfect rhymes with the updated rhyme

#  Featural Rhymes
This feature takes the perfect rhyme of a word and changes some of the consonant phones based on how close the consonants are based on featural theory

# Feature Rankings based on ARPABet (closest to phone is closest featurally)
**Phones in parentheses are not included to save memory)

- B \[b\]: P, D, (T, G, K)
- CH \[tʃ\]: SH<->JH, (T, D, K, G )
- D \[d\]: T, JH, (Z)
- DH \[ð\]: TH, V, (F)
- F \[f\]: V, TH, (DH, P, B)
- G \[g\]: K, D
- HH \[h\]: (Illegal word ending)
- JH \[dʒ\]: ZH<->CH, (D, T, G, K)
- K \[k\]: G, T, (D)
- L \[l\]: R
- M \[m\]: N, NG
- N \[n\]: NG, M
- NG \[ŋ\]: N, M
- P \[p\]: B, T
- R \[ɹ\]: L
- S \[s\]: Z, T
- SH \[ʃ\]: ZH, CH, (S, TH, Z)
- T \[t\]: D, CH, (S)
- TH \[θ\]: DH, F, (V)
- V \[v\]: F, DH
- W \[w\]: (Illegal word ending)
- Y \[j\]: (Illegal word ending)
- Z \[z\]: S, ZH
- ZH \[ʒ\]: JH, SH, (Z, DH, S)


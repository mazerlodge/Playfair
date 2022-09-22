#!/bin/bash

#Test no key
echo "---- Test no key ------"
python ../src/playfair.py -debug -enctext "stuff to decrypt"

# Test no enctext or plaintext 
echo "---- Test no plain or enc text ------"
python ../src/playfair.py -debug -key fortytwo

# Test key and phrase without spaces 
echo "---- Test key and phrase without spaces ------"
python ../src/playfair.py -debug -key fortytwo -enctext keyAndPhraseNoSpaces

# Test key and phrase with spaces 
echo "---- Test key and phrase with spaces ------"
python ../src/playfair.py -debug -key fortytwo -enctext "phrase goes here"

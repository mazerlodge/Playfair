#!/bin/bash

#Test no key
echo "---- 1 Test no key ------"
python ../src/playfair.py -debug -enctext "stuff to decrypt"

# Test no enctext or plaintext 
echo "---- 2 Test no plain or enc text ------"
python ../src/playfair.py -debug -key fortytwo

# Test key and phrase without spaces 
echo "---- 3 Test key and phrase without spaces ------"
python ../src/playfair.py -debug -key fortytwo -enctext keyAndPhraseNoSpaces

# Test key and phrase with spaces 
echo "---- 4 Test key and enctext with spaces ------"
python ../src/playfair.py -debug -key fortytwo -enctext "enc phrase goes here"

# Test key and phrase with spaces 
echo "---- 5 Test key and plaintext with spaces ------"
python ../src/playfair.py -debug -key fortytwo -plaintext "plain phrase goes here"

#!/bin/bash

#Test no key
echo "Test no key"
python ../src/playfair.py -debug -enctext "stuff to decrypt"

# Test no enctext or plaintext 
echo "Test no plain or enc text"
python ../src/playfair.py -debug -key fortytwo

#!/bin/bash

# Test key and phrase with spaces 
echo "---- 0 Test key and plaintext with spaces ------"
python ../src/playfair.py -debug -key fortytwo -plaintext "plain phrase goes here"

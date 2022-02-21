# Simple Wordle Solver

A simple program to help you play wordle. Python 3 is the only requirement. Run the program with:

```
python main.py
```

The program provides you with a word to guess, then expects you to input some information from the wordle game so it can provide you with the next word you should guess. This continues until you get the correct word or the problem becomes over-constrained and the program outputs "no match!". You can stop the program with ctrl-C.

You communicate with the program by typing 5 numbers and hitting enter. The 5 numbers correspond to the five letters in the word you just put into wordle. The numbers can be 0, 1, or 2. 0 corresponds to grey, 1 corresponds to yellow, and 2 corresponds to green. For example, if you guess HYPER and the correct word is OTHER, then wordle will color the H yellow, the Y and P grey, and the E and R green. So you would type "10022" for yellow-grey-grey-green-green and hit enter.

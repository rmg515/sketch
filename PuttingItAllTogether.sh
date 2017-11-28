#!/bin/bash   


echo "Here is what I learned on Day 1"

echo "I am going to go to the / directory"
cd /

echo "and home again" 
cd

echo "I am going to copy the blah.txt file" 
cp blah.txt blah2.txt

echo "I am going to rename blah2 to RobyIsAwesome"
mv blah2.txt RobyIsAwesome.txt

echo "vi is a bleedin misery" 
echo "You get to Insert mode by typing 'i'" 
echo "You exit Insert mode by pressing Esc" 
echo "I can highlight lines with Shift+v -- and arrows to highlight EVEN MORE lines!" 
echo "I can get back to command mode with Esc" 
echo "Writing ('saving')  then quitting is done by ':wq' "

echo "I can check where I am by pwd" 
echo "(A tilde on the left means I'm in the home directory!)"
pwd 

echo "I can see more detail in a list with..."
ls -l 

echo "Read files by 'more' or 'less' (doesn't matter, but "more" seems less annoying"'! HA!)' 

echo "Run a script \(like this one\!\) by pressing ."

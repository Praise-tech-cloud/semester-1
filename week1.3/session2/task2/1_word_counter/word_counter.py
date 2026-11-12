# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210

file = input("give me one of the 3 file's names please:").lower()

if file == "glasses" or file == "glasses.txt":
    with open("glasses.txt", "r") as infile:
        List = [line.strip().split()for line in infile]   
        wordcount = 0
        for i in List:
            for ii in i:
                wordcount += 1
        print(f"{wordcount} words in the glasses file")

elif file == "story" or file == "story.txt":
    with open("story.txt", "r") as infile:
        List = [line.strip().split()for line in infile]   
        wordcount = 0
        for i in List:
            for ii in i:
                wordcount += 1
        print(f"{wordcount} words in the story file")

elif file == "story2" or file == "story2.txt":
    with open("story2.txt", "r") as infile:
        List = [line.strip().split()for line in infile]   
        wordcount = 0
        for i in List:
            for ii in i:
                wordcount += 1
        print(f"{wordcount} words in the story2 file")

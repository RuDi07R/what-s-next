import itertools 
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

# if the word entered is same then 

file = open("data.txt", "r") 
data = file.read().split("\n")
list = []
for line in data:
    new = line.split(" ")
    for j in range(len(new)):
        list.append(new[j])

noDup = set(list)
possible = prompt("Enter the word: ", completer=WordCompleter(noDup, ignore_case=True))
sentence = possible

while True:

    freq = {}
    total = 0
    for i in range(len(list)):
        if list[i] == possible:  # Check if the word is in the list
            if list[i+1] not in freq:  # Check if the word is in the dictionary
                freq[list[i+1]] = 1  # Add the word to the dictionary
                total += 1  
            else:
                freq[list[i+1]] += 1  # Increment the word count
                total += 1
    probability = {}
    for i in list:
        if i in freq:  # Check if the word is in the dictionary
            probability[i] = freq[i]/total  # Calculate the probability
        else:
            continue
            
    sortedDic = sorted(probability.items(), key=lambda x: x[1], reverse=True)
    sortedDic = dict(sortedDic)

    # print(f"The next words after '{possible}' can be: ")
    print()
    print("----------------------------------------------------------------------------------------------------------")
    print("The current sentence is: ", sentence)
    print("----------------------------------------------------------------------------------------------------------")
    print()
    # Print the top 5 hightest probability words
    N = 6
    word_list = []
    for i in itertools.islice(sortedDic.keys(), N):
        print("|------------------|")
        print("   "+i)
        word_list.append(i)
        word_completer = WordCompleter(noDup, ignore_case=True)
        word_completer = WordCompleter(word_list)
        
    print("|------------------|")
    print()
    

    next_word = prompt("Enter the next word or '//exit' to exit the Application or '//clear' to reset the sentence: ", completer=word_completer)
    if len(next_word.split()) > 1:
        possible = next_word.split()[-1]
    else:
        possible = next_word
    sentence += " " + next_word
    
    if next_word == "//exit":
        break
    elif next_word == "//clear":
        sentence = ""

    os.system('cls' if os.name == 'nt' else 'clear')

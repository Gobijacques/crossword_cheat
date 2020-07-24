    #opening the word list and storing it in a variable
    
file1 = open("francais.txt","r")
wordlist = file1.read().splitlines()

def search(clue):

    results=[]
    real_letters=[]
    cluenum=int(0)

    #generating a list that stores the known letters from the give clue
    #and stores them as well as their position by filtering out unknown letters

    for clue_char in clue:
        if clue_char!='$':
            real_letters.append([clue_char,cluenum])
        cluenum+=1

    #selecting the words that fit with the known letters

    for word in wordlist:
        if len(word)==len(clue):
            if all(word[char[1]]==char[0] for char in real_letters):
                results.append(word)

    #prompting the user before printing results in a single column
    #not to flood the console if the result number is too high

    print(len(results),'results. Proceed? (y)')

    if input()=='y':
        print('\n'.join(results))

    return None

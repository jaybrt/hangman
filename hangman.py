import random
hangpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def getWord():
    l = []

    with open('sowpods.txt', 'r') as f:
        for line in f.readlines():
            l.append(line.strip())
    return l[random.randint(0,len(l))]



if __name__ == '__main__':
    
    word = getWord()
    strikes = 0
    gl = []
    guessed = False

    print(hangpics[0])
    print(len(word)*'_')

    while guessed == False:
        if strikes == 6:
            print(f'You lose the word was {word}')
            break
        
        guess = input('Guess Letter:').upper()
        if guess not in gl:
            gl.append(guess)
            if guess not in word:
                strikes +=1
            pw = ''
            for l in word:
                if l in gl:
                    pw += l
                else:
                    pw += '_'

            if pw == word:
                guessed = True
                print(pw)
                print('You got it')

            else:
                print(hangpics[strikes])
                print(pw)
                print([i for i in gl if i not in word])
            

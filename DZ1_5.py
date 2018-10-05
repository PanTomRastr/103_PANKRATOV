print('Enter word')

def polindrom(word):
    if word==word[::-1]:
        print(word)
        print('This word is polindrom')
    else:
        
        print('This word is not polindrom')
polindrom(input())
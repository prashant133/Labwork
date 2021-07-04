'''
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.
'''
def palin() :
    a = input('enter the string')
    revstr = (a[::-1])
    print(revstr)
    if revstr == a :
        print('this is palindrome')
    else :
        print('Not palindrome')
palin()
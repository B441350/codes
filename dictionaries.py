def launch_missiles():
    print("missiles_launched")

launch_missiles()

#
def even_or_odd (n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")


w = print (even_or_odd(31))

##docstrings are used to document our code
#used right after the definition of a function,
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

#here the square documentation can be acccessed by using __doc__attributes
print(square.__doc__)

#

from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:

            story_words.append(word)
    story.close()
    return story_words

#definig new function that is print words
def print_words(story_words):
    for word in story_words:
        print(word)
def main():
    words = fetch_words()
    print(word)

if __name__ == '__main__':
   main()

from words import(fetch_words,print_words)
print_words(fetch_words())






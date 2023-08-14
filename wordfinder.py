"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''Maching for finding random words from dictionary words.txt
    
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True
    '''

    def __init__(self, path):
        '''Read the dictionary and print the amount of words read'''
        dict_file=open(path)
        self.words=self.parse(dict_file)
        print(f'{len(self.words)} words read')

    def parse(self, dict_file):
        '''Parse list of words to dict_file'''
        return [w.strip() for w in dict_file]
    
    def random(self):
        '''Return a random word'''
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    >>> swf = SpecialWordFinder("veggies.txt")
    4 words read

    >>> swf.random() in swf.words
    True

    >>> swf.random() in swf.words
    True

    >>> swf.random() in swf.words
    True
    """
    
    def parse(self, dict_file):
        '''Parse list of words to dict_file, skipping blank lines and # lines'''
        return [w.strip() for w in dict_file 
                if w.strip() and not w.startswith("#")]
# """Word Finder: finds random words from a dictionary."""
# import random
# class WordFinder:
#     ...
#     def __init__(self,path):
#         self.path = 
import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(r'D:\My Projects\Coding\Bootcamp work\Learning coding\Learning Units\Unit_19_Python\python-oo-practice\python-oo-practice\words.txt')

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

# Example usage:
wf = WordFinder('words.txt')
print(wf.random())  # This should print a random word


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
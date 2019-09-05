import random
import string
import json

class Generator:
    """
    Generates a random password string. Has 5 arguments: 
        size: int
        lowercase: boolean
        uppercase: boolean
        numbers: boolean
        symbols: boolean
    Note: All booleans are true and size is 16 in default state.

    Functions:
        pass_gen: returns a random password string.
    """

    def __init__(self, size=16, lowercase=True, uppercase=True, numbers=True, symbols=True):
        self.all_chars = []
        self.size = size

        if lowercase:
            self.all_chars += {x for x in string.ascii_letters.lower()}

        if uppercase:
            self.all_chars += {x for x in string.ascii_letters.upper()}

        if numbers:
            self.all_chars += {x for x in string.digits}

        if symbols:
            self.all_chars += {'!','@','#','$','%','^','&','_','-','+','=','?'}

    def pass_gen(self):
        pass_string = ""

        for i in range(self.size):
            random.seed(int(random.random() * 100000))
            pass_string += random.choice(self.all_chars)

        pass_list = list(pass_string)
        random.shuffle(pass_list)

        return ''.join(pass_list)

class Helper:
    """
    Creates a helper string, consisting of words to correspond each character of the password, to ease in oral
    memorization. Has 2 arguments:
        password: string
        filenames: array
    Note: Files are not checked, and the program can fail if file is not found.
    Functions:
        wordlist: Returns an array of all words from the input of "filenames".
        mem_string: Returns the memory_string
    """

    def __init__(self, password, filenames):
        self.pass_string = password
        self.filelist = filenames
        self.numbers = {x for x in string.digits}
        self.symbols = {'!','@','#','$','%','^','&','_','-','+','=','?'}

        self.num_dict = json.loads(open("assets/numbers.json",'r').read())
        self.sym_dict = json.loads(open("assets/symbols.json",'r').read())

    def wordlist(self):
        h_words = []
        for filename in self.filelist:
            with open(filename,"r") as h_file:
                words = h_file.readlines()

            for word in words:
                # Remove newlines
                no_newline = [x for x in word[:-1]]
                h_words.append(''.join(no_newline))

        return h_words

    def mem_string(self):
        delta = []
        memstring = ""

        for char in self.pass_string:
            subset = []
            # Add words with same starting character to a list
            for word in self.wordlist():
                if word[0].lower() == char.lower():
                    if char.islower():
                        subset.append(word.lower())
                    elif char.isupper():
                        subset.append(word.upper())

            # Add them to list delta
            if subset:
                delta.append(subset)

            if char in self.numbers:
                delta.append([self.num_dict[char]])
            if char in self.symbols:
                delta.append([self.sym_dict[char]])

        # Adding a random word from subset to memstring
        for subset in delta:
            if len(subset) > 1:
                memstring += (random.choice(subset) + " ")
            else:
                memstring += (subset[0] + " ")

        return memstring


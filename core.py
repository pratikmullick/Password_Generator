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
            pass_string += random.choice(self.all_chars)

        return pass_string

class Helper:
    """
    Creates a helper string, consisting of words to associate each character of the password, to ease in oral
    memorization of the password. Has 2 arguments:
        password: string
        filenames: array
    Note: Files are not checked, and the program can fail if file is not found.
    """

    def __init__(self, password, filenames):
        self.pass_string = password
        self.filelist = filenames
        self.num_dict = json.loads(open("numbers.json",'r').read())
        self.sym_dict = json.loads(open("symbols.json",'r').read())

    def wordlist(self):
        h_words = []
        for filename in self.filelist:
            with open(filename,"r") as h_file:
                words = h_file.readlines()

            for word in words:
                correct = [x for x in word[:-1]]
                h_words.append(''.join(correct))

        return h_words

    def helper_string(self):
        delta = []
        h_string = ""

        for i in self.pass_string:
            subset = []
            for word in self.helper_words:
                if word[0].lower() == i.lower():
                    subset.append(word)
            delta.append(subset)

        for subset in delta:
            h_string += (random.choice(subset) + " ")

        return h_string


# Debug
if __name__ == "__main__":
    gen = Generator().pass_gen()
    file_list = ["names.txt","countries.txt"]
    helper = Helper(gen, file_list)

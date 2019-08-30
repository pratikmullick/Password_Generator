import random
import string

class Generator:

    def __init__(self, size=16, l_flag=True, n_flag=True, p_flag=True):
        self.all_chars = []
        self.size = size

        if l_flag:
            self.all_chars += {x for x in string.ascii_letters}
        
        if n_flag:
            self.all_chars += {x for x in string.digits}

        if p_flag:
            self.all_chars += {'!','@','#','$','%','^','&','_','-','+','=','<','>',':','?'}

    def passgen(self):
        pass_string = ""

        for i in range(self.size):
            pass_string += random.choice(self.all_chars)

        return pass_string

class Helper:

    def __init__(self, pass_string, filenames):
        self.pass_string = pass_string
        self.filelist = filenames
        self.helper_words = self.wordlist()

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
    gen = Generator(16,True, False, False).passgen()
    helper = Helper(gen, ["names.txt","countries.txt"])

    print(helper.helper_string())

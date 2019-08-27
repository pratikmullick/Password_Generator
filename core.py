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
            self.all_chars += {'!','@','#','$','%','^','&','*','_','-','+','=','?','<','>',':'}

    def passgen(self):
        pass_string = ""

        for i in range(self.size):
            pass_string += random.choice(self.all_chars)

        return pass_string

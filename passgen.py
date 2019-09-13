#!/usr/bin/env python3
import argparse
import os
from core import *

def CommandLine():

    cwd = os.path.expanduser('~') + "/Python/Password_Generator/"
    
    description = "Passgen: A Random Password Generator"

    parser = argparse.ArgumentParser(description=description, prog="PassGen")
    parser.add_argument("-s", "--size", type=int, help="Number of characters in generated password")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.50")
    parser.add_argument("-u", "--upper", help="Use uppercase characters", action="store_true", default=True)
    parser.add_argument("-n", "--numbers", help="Use digits", action="store_true", default=True)
    parser.add_argument("-p", "--symbols", help="Use symbols", action="store_true")
    parser.add_argument("-d", "--defaults", help="Use optimized defaults", action="store_true")
    parser.add_argument("-m", "--verbose", help="Shows memorization text", action="store_true")

    args = parser.parse_args()

    if args.size or args.defaults:
        size = args.size
    else:
        size = int(input("Enter length of password: "))

    if args.defaults:
        gen = Generator(32, True, True, True, True)
    else:
        gen = Generator(size, True, args.upper, args.numbers, args.symbols)

    password = gen.pass_gen()
    print(password)

    if args.verbose:
        memo = Helper(password, [cwd + "assets/names.txt",cwd + "assets/countries.txt"]).mem_string()
        print(memo)

if __name__ == "__main__":
    CommandLine()

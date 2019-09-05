#!/usr/bin/env python3
import argparse
from core import *

def CommandLine():

    epilog = open("LICENSE",'r').read()

    parser = argparse.ArgumentParser(epilog=epilog, prog="PassGen")
    parser.add_argument("-s", "--size", type=int, help="Number of characters in generated password")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.50")
    parser.add_argument("-uc", help="Use uppercase characters", action="store_true", default=True)
    parser.add_argument("-n", help="Use digits", action="store_true", default=True)
    parser.add_argument("-sb", help="Use symbols", action="store_true")
    parser.add_argument("--defaults", help="Use optimized defaults", action="store_true")
    parser.add_argument("--verbose", help="Shows memorization text", action="store_true")

    args = parser.parse_args()

    if args.size or args.defaults:
        size = args.size
    else:
        size = int(input("Enter length of password: "))

    if args.defaults:
        gen = Generator(16, True, True, True, True)
    else:
        gen = Generator(size, True, args.uc, args.n, args.sb)

    password = gen.pass_gen()
    print(password)
    
    if args.verbose:
        memo = Helper(password, ["assets/names.txt","assets/countries.txt"]).mem_string()
        print(memo)

if __name__ == "__main__":
    CommandLine()


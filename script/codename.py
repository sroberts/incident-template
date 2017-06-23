#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import requests

words = open('/usr/share/dict/words').readlines()

def generate_codename():
    return "{}-{}".format(random.choice(words).strip(), random.choice(words).strip())

def main():
    """Where the business gets done"""
    print("investigation-{}".format(generate_codename()))

if __name__ == '__main__':
    main()

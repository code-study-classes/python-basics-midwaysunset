import os
import re

def extract_file_name(full_file_name):
    base = os.path.basename(full_file_name)  # example.txt
    name, _ = os.path.splitext(base)         # ('example', '.txt')
    return name

def encrypt_sentence(sentence):
    even_chars = sentence[::2]  # символы на четных позициях
    odd_chars = sentence[1::2]  # символы на нечетных позициях
    return even_chars + odd_chars[::-1]

def check_brackets(expression):
    stack = []
    for idx, char in enumerate(expression):
        if char == '(':
            stack.append(idx)
        elif char == ')':
            if not stack:
                return idx
            stack.pop()
    if stack:
        return -1
    return 0

def reverse_domain(domain):
    return '.'.join(reversed(domain.split('.')))

def count_vowel_groups(word):
    vowels = 'aeiouy'
    word = word.lower()
    groups = re.findall(r'[aeiouy]+', word)
    return len(groups)

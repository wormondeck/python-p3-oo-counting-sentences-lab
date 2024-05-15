#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value = ''):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self.value = value

    def is_sentence(self):
        return self._value and self._value[-1] == '.'
        
    def is_question(self):
        return self.value and self.value[-1] == '?'
           
    def is_exclamation(self):
        return self.value and self.value[-1] == '!'
    
    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self._value = new_value
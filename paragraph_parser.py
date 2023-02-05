from typing import Dict, List, Set
from collections import defaultdict
import re
import string

class ParagraphParser:

    alphanumeric_characters = set(string.ascii_letters + string.digits + ' ')

    def __init__(self,paragraph):
        self.paragraph = paragraph
        self.tokenized_paragraph = self._get_all_valid_words(paragraph)
        self.all_characters = self._get_all_valid_characters(paragraph)


    def _get_all_valid_words(self, paragraph: str) -> List[str]:
        words = paragraph.split()
        valid_words = []

        # strip punctuation from start and end of words
        words = [w.strip(string.punctuation) for w in words]
        
        for word in words:
            chars = [c for c in word]
            if chars and all([c in self.alphanumeric_characters for c in chars]):
                valid_words.append(word.lower())
        return valid_words


    def _get_all_valid_characters(self,paragraph: str) -> List[str]:
        return [
            char_ for char_ in paragraph 
            if char_ in self.alphanumeric_characters 
            or char_ in string.punctuation
        ]


    def get_word_frequency(self) -> Dict[str,int]:
        """count the repetition of each word (alphanumeric). 
        the characters array should contain only English words and numbers 
        and they should be alphabetically ordered 
        (numbers first followed by words)."""
        word_freq = defaultdict(lambda :0)
        for token in self.tokenized_paragraph:
            word_freq[token] += 1
        return dict(sorted(word_freq.items()))


    def get_word_count(self) -> int:
        """get the total number of valid words in the paragraph."""
        return len(self.tokenized_paragraph)
    

    def get_character_count(
        self, 
        exclude: Set[str]=set()
    ) -> int:
        """"return the total number of characters. 
        if exclude is not empty, the total number of occurences of characters 
        not in the set will be returned.
        if both include and exclude are empty, the total number of characters will be returned.
        """
        filtered_characters = [char for char in self.all_characters if char not in exclude]
        return len(filtered_characters)

        

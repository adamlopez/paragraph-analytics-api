import pytest
from paragraph_parser import ParagraphParser
import re


def test_characters_all_valid():
    paragraph = "one 1 day also "
    parser = ParagraphParser(paragraph)
    assert  parser.tokenized_paragraph == ['one','1','day','also']


def test_exclude_foreign_characters():
    paragraph = "word 是 word2"
    parser = ParagraphParser(paragraph)
    assert  parser.tokenized_paragraph == ['word','word2']
    

def test_exclude_emojis():
    paragraph = "abcdefg123 👀aa 🙂"
    parser = ParagraphParser(paragraph)
    assert  parser.tokenized_paragraph == ['abcdefg123']

def test_exclude_multiple_spaces():
    paragraph = "abcdefg123    another word"
    parser = ParagraphParser(paragraph)
    assert  parser.tokenized_paragraph == ['abcdefg123','another','word']

def test_word_count():
    paragraph =  'this is a test this this this'
    parser = ParagraphParser(paragraph)
    word_freq = parser.get_word_frequency()
    assert word_freq == {'a': 1,'is': 1,'test':1,'this': 4}


def test_word_count_with_numbers():
    paragraph =  'this is a test 4 this 4 this this 123'
    parser = ParagraphParser(paragraph)
    word_freq = parser.get_word_frequency()
    assert word_freq == {'123': 1, '4':2, 'a': 1,'is': 1,'test':1,'this': 4}


def test_word_count_uppercase_lowercase():
    paragraph =  'this is a test. This is a test. Test.'
    parser = ParagraphParser(paragraph)
    word_freq = parser.get_word_frequency()
    print(word_freq)
    assert word_freq == {'a': 2, 'is':2, 'test': 3,'this': 2}


def test_init_character_array():
    paragraph =  ' this is a test 4 '
    parser = ParagraphParser(paragraph)
    assert parser.all_characters == \
        [' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', '4', ' ']

def test_get_character_count():
    paragraph =  ' this is a test 4 '
    parser = ParagraphParser(paragraph)
    assert parser.get_character_count() == 18

def test_get_character_count_no_spaces():
    paragraph =  ' this is a test 4 '
    parser = ParagraphParser(paragraph)
    assert parser.get_character_count(exclude={' '}) == 12

def  test_get_word_count():
    paragraph =  'this is a test 4 '
    parser = ParagraphParser(paragraph)
    assert parser.get_word_count() == 5


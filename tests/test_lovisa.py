import pytest
from lovisa import Lovisa

def test_she_has_a_title():
    lovisa = Lovisa('Lovisa the Swedish Goddess')
    assert lovisa.title == 'Lovisa the Swedish Goddess'

def test_she_is_brilliant_by_default():
    lovisa = Lovisa('Lovisa the Mentor')
    assert lovisa.characteristics == ('brilliant')
    assert lovisa.is_brilliant() == True

def test_she_is_more_than_brillian():
    lovisa = Lovisa('Lovisa the friend', ['brilliant', 'kind'])
    assert lovisa.characteristics == ['brilliant', 'kind']
    assert lovisa.is_brilliant() == True
    assert lovisa.is_kind() == True

def test_she_says_sparkly_stuff():
    lovisa = Lovisa('Lovisa the Loved')
    assert lovisa.say('Wonderful!') == '**;* Wonderful! **;*'
    assert lovisa.say('You are doing great!') == '**;* You are doing great! **;*'
    
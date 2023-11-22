import pytest
from unicorn import Unicorn

# @pytest.mark.skip
def test_it_has_a_name():
    unicorn = Unicorn('Robert')
    assert(unicorn.name) == 'Robert'

# @pytest.mark.skip
def test_it_is_silver_by_default():
    unicorn = Unicorn('Margaret')
    assert(unicorn.color)

# @pytest.mark.skip
def test_it_doesnt_have_to_be_silver():
    unicorn = Unicorn('Barbara', 'purple')
    assert(unicorn.color) == 'purple'
    assert(unicorn.is_silver()) == False

# @pytest.mark.skip
def test_it_says_sparkly_stuff():
    unicorn = Unicorn('Johnny')
    assert(unicorn.say('Wonderful!')) == '**;* Wonderful! **;*'
    assert(unicorn.say('I dont like you very much.')) == '**;* I dont like you very much. **;*'
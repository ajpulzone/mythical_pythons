import pytest
from dragon import Dragon

# @pytest.mark.skip
def test_it_has_a_name():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')
    assert(dragon.name) == 'Ramoth'

def test_it_has_a_rider():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')
    assert(dragon.rider) == 'Lessa'

def test_it_has_a_color():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')
    assert(dragon.color) == 'gold'

def test_it_is_a_different_dragon():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert(dragon.name) == 'Mnementh'

def test_it_has_a_different_rider():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert(dragon.rider) == 'Flar'

def test_it_has_a_different_color():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert(dragon.color) == 'bronze'

def test_it_was_born_hungry():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert(dragon.is_hungry()) == True

def test_it_eats_alot():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')
    assert(dragon.is_hungry()) == False
    dragon.eat()
    assert(dragon.is_hungry()) == False
    dragon.eat()
    assert(dragon.is_hungry()) == False
    dragon.eat()
    assert(dragon.is_hungry()) == True

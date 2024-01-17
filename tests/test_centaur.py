import pytest
from centaur import Centaur

# @pytest.mark.skip
def test_it_has_a_name():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.name) == 'George'

# @pytest.mark.skip
def test_it_has_a_horse_breed():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.breed) == 'Palomino'

# @pytest.mark.skip
def test_it_has_excellent_bow_skills():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.shoot()) == 'Twang!!!'

# @pytest.mark.skip
def test_it_makes_a_horse_sound_when_it_runs():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.run()) == 'Clop clop clop clop!'

# @pytest.mark.skip
def test_when_it_is_first_created_it_is_not_cranky():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.is_cranky()) == False

# @pytest.mark.skip
def test_when_it_is_first_created_it_is_standing_up():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.is_standing) == True

# @pytest.mark.skip
def test_it_gets_tired_after_running_or_shooting_a_bow_thrice():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.is_cranky()) == False

    centaur.run()
    centaur.shoot()
    centaur.run()
    assert(centaur.is_cranky()) == True

# @pytest.mark.skip
def test_it_will_not_shoot_a_bow_when_cranky():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.is_cranky()) == False

    # We used a _ operator - it's used when
    # we really don't care about the name of
    # the iterator (the "_")
    for _ in range(3):
        centaur.shoot()
    assert(centaur.shoot()) == 'NO!'

# @pytest.mark.skip
def test_it_will_not_sleep_when_it_is_standing():
    centaur = Centaur('George', 'Palomino')
    assert(centaur.sleep()) == 'NO!'

# @pytest.mark.skip
def test_it_is_not_standing_after_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()
    assert(centaur.is_standing) is False
    assert(centaur.is_laying) == True

# @pytest.mark.skip
def test_it_can_sleep_when_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()
    assert(centaur.sleep()) != 'NO!'

# @pytest.mark.skip
def test_it_cannot_shoot_a_bow_when_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()
    assert(centaur.shoot()) == 'NO!'

# @pytest.mark.skip
def test_it_cannot_run_while_laying_down():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()
    assert(centaur.run()) == 'NO!'

# @pytest.mark.skip
def test_it_can_stand_up():
    centaur = Centaur('George', 'Palomino')
    centaur.lay_down()
    centaur.stand_up()
    assert(centaur.is_standing) == True

# @pytest.mark.skip
def test_it_is_no_longer_cranky_after_sleeping():
    centaur = Centaur('George', 'Palomino')
    centaur.shoot()
    centaur.run()
    centaur.shoot()
    assert(centaur.is_cranky()) == True

    centaur.lay_down()
    centaur.sleep()
    assert(centaur.is_cranky()) == False

    centaur.stand_up()
    assert(centaur.shoot()) == 'Twang!!!'
    assert(centaur.run()) == 'Clop clop clop clop!'

'''
# (Now you'll write your own tests!)
  it 'becomes rested after drinking a potion' do
    # your code here
  end

  it 'can only drink a potion whilst standing' do
    # your code here
  end

  it 'gets stick if a potion is drunk while rested' do
    # your code here
  end
end
'''
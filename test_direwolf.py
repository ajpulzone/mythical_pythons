import pytest
from direwolf import Direwolf, Stark

def test_it_has_a_name():
    wolf = Direwolf('Nymeria')
    assert wolf.name == 'Nymeria'

def test_it_can_have_a_different_name_and_can_have_a_home():
    wolf = Direwolf('Lady')

    assert wolf.home == 'Beyond the Wall'
    assert wolf.name == 'Lady'

def test_it_is_massive_by_default():
    wolf = Direwolf('Ghost')

    assert wolf.size == 'Massive'
    assert wolf.name == 'Ghost'

def test_it_can_have_another_home_and_be_another_size():
  wolf = Direwolf('Shaggydog', 'Winterfell', 'Smol Pupper')

  assert wolf.name == 'Shaggydog'
  assert wolf.home == 'Winterfell'
  assert wolf.size == 'Smol Pupper'

def test_that_the_starks_are_in_winterfell_by_default():
  wolf = Direwolf('Summer', 'Winterfell')
  stark = Stark('Bran')

  assert wolf.home == 'Winterfell'
  assert stark.location == 'Winterfell'

def test_a_direwolf_starts_with_no_starks_to_protect():
  wolf = Direwolf('Nymeria')
  stark = Stark('Arya')

  assert len(wolf.starks_to_protect) == 0

def test_a_direwolf_can_protect_the_stark_children():
  wolf = Direwolf('Nymeria', 'Riverlands')
  stark = Stark('Arya', 'Riverlands')

  wolf.protects(stark)

  assert wolf.starks_to_protect[0].name == 'Arya'

def test_a_direwolf_can_only_protect_the_stark_children_if_they_are_in_the_same_location():
  wolf = Direwolf('Ghost')
  stark = Stark('Jon', 'Kings Landing')

  wolf.protects(stark)
  assert(len(wolf.starks_to_protect)) == 0
  '''

  it 'can only protect the Stark Children if they are in the same location' do
    wolf = Direwolf.new('Ghost')
    stark = Stark.new('Jon', 'Kings Landing')

    wolf.protects(stark)

    expect(wolf.starks_to_protect).to be_empty
  end

  it 'can only protect two Starks at a time' do
    summer_wolf = Direwolf.new('Summer', "Winterfell")
    lady_wolf = Direwolf.new('Lady', "Winterfell")
    sansa_stark = Stark.new('Sansa')
    jon_stark = Stark.new('Jon')
    rob_stark = Stark.new('Rob')
    bran_stark = Stark.new('Bran')
    arya_stark = Stark.new('Arya')

    summer_wolf.protects(sansa_stark)
    summer_wolf.protects(jon_stark)
    lady_wolf.protects(rob_stark)
    lady_wolf.protects(bran_stark)
    lady_wolf.protects(arya_stark)

    expect(summer_wolf.starks_to_protect).to include(sansa_stark)
    expect(summer_wolf.starks_to_protect).to include(jon_stark)
    expect(lady_wolf.starks_to_protect).to include(rob_stark)
    expect(lady_wolf.starks_to_protect).to include(bran_stark)
    expect(lady_wolf.starks_to_protect).to_not include(arya_stark)
  end

  it 'the Starks are unsafe by default' do
    stark = Stark.new('Jon', 'The Wall')

    expect(stark.safe?).to be false
    expect(stark.house_words).to eq('Winter is Coming')
  end

  it 'protects the Starks' do
    wolf = Direwolf.new('Nymeria', "Winterfell")
    arya_stark = Stark.new('Arya')
    sansa_stark = Stark.new('Sansa')

    wolf.protects(arya_stark)

    expect(arya_stark.safe?).to be true
    expect(sansa_stark.safe?).to be false
  end

  it 'hunts white walkers' do
    wolf = Direwolf.new('Nymeria', 'Winterfell')

    expect(wolf.hunts_white_walkers?).to be true
  end

  it 'will not hunt white walkers when protecting Starks' do
    wolf = Direwolf.new('Nymeria', "Winterfell")
    arya_stark = Stark.new('Arya')

    wolf.protects(arya_stark)

    expect(wolf.hunts_white_walkers?).to be false
  end

  it 'can leave and stop protecting Starks' do
    summer_wolf = Direwolf.new('Summer', "Winterfell")
    lady_wolf = Direwolf.new('Lady', "Winterfell")
    sansa_stark = Stark.new('Sansa')
    arya_stark = Stark.new('Arya')

    summer_wolf.protects(arya_stark)
    lady_wolf.protects(sansa_stark)
    summer_wolf.leaves(arya_stark)

    expect(summer_wolf.starks_to_protect).to be_empty
    expect(lady_wolf.starks_to_protect.first.name).to eq('Sansa')
    expect(arya_stark.safe?).to be false
  end

  it 'returns the Stark object when it leaves' do
    summer_wolf = Direwolf.new('Summer', "Winterfell")
    lady_wolf = Direwolf.new('Lady', "Winterfell")
    sansa_stark = Stark.new('Sansa')
    arya_stark = Stark.new('Arya')
    rickon_stark = Stark.new('Rickon')

    summer_wolf.protects(arya_stark)
    lady_wolf.protects(sansa_stark)
    summer_wolf.leaves(arya_stark)

    expected = lady_wolf.leaves(rickon_stark)

    expect(expected.name).to eq('Rickon')
  end

end

'''
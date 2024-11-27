import pytest

from cosmere.weapons import Dice, DamageTypes, Ranges, Traits, Weapons


@pytest.mark.parametrize('weapon', Weapons)
def test_weapons(weapon):
    # assert weapon.category in Categories
    assert weapon.damage_type in DamageTypes
    assert weapon.range in Ranges

    # for dmg in weapon.damage:
    #     assert dmg in Dice

    for trait in weapon.traits:
        assert trait in Traits

    # for trait in weapon.expert_traits:
    #     assert trait in Traits

    # highest_roll = sum([d.sides for d in weapon.damage])
    # for _ in range(1000):
    #     assert 1 <= weapon.roll_damage() <= highest_roll


@pytest.mark.parametrize('die', Dice)
def test_dice(die):
    for _ in range(1000):
        assert 1 <= die.roll() <= die.sides

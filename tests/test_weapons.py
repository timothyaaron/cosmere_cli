import pytest

from cosmere.weapons import Categories, Dice, DamageTypes, Ranges, Traits, Weapons


@pytest.mark.parametrize('weapon', Weapons)
def test_attributes(weapon):
    """Verify Weapon attributes are of the necessary types"""
    assert weapon.category in Categories
    assert weapon.damage_type in DamageTypes
    assert weapon.range in Ranges

    for dmg in weapon.damage:
        assert dmg in Dice

    for trait in weapon.traits:
        assert trait in Traits

    for trait in weapon.expert_traits:
        assert trait in Traits


@pytest.mark.parametrize('weapon', Weapons)
def test_roll_damage(weapon):
    """Verify Weapon rolls are valid"""
    highest_roll = sum([d.sides for d in weapon.damage])
    for _ in range(1000):
        assert 1 <= weapon.roll_damage() <= highest_roll


@pytest.mark.parametrize('die', Dice)
def test_dice(die):
    """Verify Dice rolls are valid"""
    for _ in range(1000):
        assert 1 <= die.roll() <= die.sides

from cosmere.character import Character
from cosmere.cultures import Cultures


def test_cli():
    """Verify build process is functional."""
    ch = Character("Adam")
    ch.culture = Cultures.NATAN

    assert f"{ch}" == "Adam is Natan"

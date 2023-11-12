from utils import both_ends, donuts, fix_start, mix_up


def test_donuts_keves():
    assert donuts(4) == "Fánkok száma: 4"
    assert donuts(9) == "Fánkok száma: 9"
    assert donuts(0) == "Fánkok száma: 0"


def test_donuts_sok():
    assert donuts(10) == "Fánkok száma: sok"
    assert donuts(99) == "Fánkok száma: sok"


def test_both_ends_empty():
    assert both_ends("") == ""
    assert both_ends("a") == ""


def test_both_ends_not_empty():
    assert both_ends("spring") == "spng"
    assert both_ends("Hello") == "Helo"
    assert both_ends("xyz") == "xyyz"


def test_fix_start_with_substitution():
    assert fix_start("babble") == "ba**le"
    assert fix_start("aardvark") == "a*rdv*rk"
    assert fix_start("google") == "goo*le"


def test_fix_start_without_substitution():
    assert fix_start("donut") == "donut"


def test_mix_up():
    assert mix_up("mix", "pod") == "pox mid"
    assert mix_up("dog", "dinner") == "dig donner"
    assert mix_up("gnash", "sport") == "spash gnort"
    assert mix_up("pezzy", "firm") == "fizzy perm"

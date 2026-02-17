from slp_world_interpreter.parser import parse
from slp_world_interpreter.extractor import extract


def test_extractor_canonical_names():
    wm = extract(parse("Two dogs are running."))
    names = [e.name for e in wm.entities]
    assert "Dog" in names  # singularized + capitalized


def test_extractor_normalizes_spatial():
    wm = extract(parse("The cat is on the chair."))
    rel = wm.relations[0]
    assert rel.spatial == "on"
    assert rel.subject == "Cat"
    assert rel.obj == "Chair"

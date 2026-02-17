from slp_world_interpreter.parser import parse


def test_parser_basic_entities():
    pw = parse("A red ball is on the table.")
    names = [e.name for e in pw.entities]
    assert "Ball" in names
    assert "Table" in names


def test_parser_attributes():
    pw = parse("A red ball is here.")
    ball = next(e for e in pw.entities if e.name == "Ball")
    assert ball.attributes.get("color") == "red"


def test_parser_spatial_relation():
    pw = parse("The cat is under the table.")
    rel = pw.relations[0]
    assert rel.spatial == "under"
    assert rel.subject == "Cat"
    assert rel.obj == "Table"

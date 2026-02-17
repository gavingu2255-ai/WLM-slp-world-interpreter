from slp_world_interpreter.parser import parse
from slp_world_interpreter.extractor import extract
from slp_world_interpreter.mapper import map_to_slp


def test_mapper_creates_nodes():
    wm = extract(parse("A red ball is on the table."))
    graph = map_to_slp(wm)
    assert "Ball" in graph.nodes
    assert "Table" in graph.nodes


def test_mapper_maps_position():
    wm = extract(parse("The cat is under the table."))
    graph = map_to_slp(wm)
    cat = graph.nodes["Cat"]
    assert any("under(Table)" in p for p in cat.positions)

from slp_world_interpreter.api import interpret


def test_end_to_end_scene():
    slp = interpret("A red ball is on the table.")
    assert "node Ball" in slp
    assert "color: red" in slp
    assert "position: on(Table)" in slp


def test_end_to_end_interaction():
    slp = interpret("The cat is watching the dog.")
    assert "state: watching(Dog)" in slp

from slp_world_interpreter.mapper import SLPNode, SLPGraph
from slp_world_interpreter.slp_emitter import emit


def test_emitter_basic_output():
    graph = SLPGraph(nodes={
        "Ball": SLPNode(
            name="Ball",
            attributes={"color": "red"},
            states=["rolling"],
            positions=["on(Table)"],
        )
    })

    out = emit(graph)

    assert "node Ball" in out
    assert "color: red" in out
    assert "state: rolling" in out
    assert "position: on(Table)" in out

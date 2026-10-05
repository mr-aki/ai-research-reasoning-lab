from arlab.tools import ToolRegistry, ToolSpec


def test_tool_registry() -> None:
    registry = ToolRegistry()
    registry.register(ToolSpec("double", "Double a number.", lambda x: x * 2))
    assert registry.get("double").function(4) == 8

class Color(enum.Enum):
    """Demonstrates lowercased Enum names in YAML."""
    RED = 0
    GREEN = 1
    BLUE = 2

    @classmethod
    def yatiml_savorize(cls, node: yatiml.Node) -> None:
        if node.is_scalar(str):
            node.set_value(node.get_value().upper())

    @classmethod
    def yatiml_sweeten(cls, node: yatiml.Node) -> None:
        node.set_value(node.get_value().lower())

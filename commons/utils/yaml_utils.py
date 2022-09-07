import yaml
from yaml.resolver import BaseResolver


class AsLiteral(str):
    pass


def represent_literal(dumper, data):
    return dumper.represent_scalar(BaseResolver.DEFAULT_SCALAR_TAG, data, style="|")


def add_representer():
    yaml.add_representer(AsLiteral, represent_literal)

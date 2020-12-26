from typing import Set

from .params import ParamBase
from .values import ValueBase


# parts pre defined, parts can be added by user (iana, x-names)
class ContentLine:
    """This is the base class for every ContentLine.

    A ContentLine consists of
        * a name, specifying the kind of the ContentLine (each kind has its own class)
        * a group string, specifying a grouping by the user with no internal meaning
        * a set of valid params which this ContenLine may have (must be derived from ParamBase)
        * a value_type, specifying which value this ContentLine may have
        * a value, the actual value of the ContentLine, with type specifyed by value_type"""
    name: str = ""
    params: Set[ParamBase] = {}
    # may be set by the user when creating a content line
    group: str = ""
    value: object = None
    value_type: ValueBase = ValueBase

    def __repr__(self):
        ret = ""
        if self.group:
            ret += self.group + "."
        ret += self.name
        for param in self.params:
            ret += ";" + param.__repr__()
        ret += self.value
        return ret


# for each predefined name, there is a own class
class SOURCE(ContentLine):
    name = "SOURCE"

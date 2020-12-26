# baseclass of every valid param value type
class ValueBase:
    """This is the base class for every valid ContentLine value.

    Every ContentLine may have multiple values, depending on the kind of the ContentLine.
    Every valid value of a ContentLine must be derived from this base class.
    """
    pass


class TextValue(ValueBase):
    pass

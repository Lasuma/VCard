class ParamBase:
    """This is the base class of every valid ContentLine parameter.

    Every ContentLine may have multiple parameters, depending on the kind of the ContentLine.
    Every valid param must be derived from this base class.
    """
    name: str = ""

    def __repr__(self):
        raise NotImplementedError


class LanguageParam(ParamBase):
    pass

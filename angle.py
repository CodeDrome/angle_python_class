from types import MappingProxyType
import math


class Angle(object):

    """
    The Angle class stores an angle value
    in a selection of units,
    and provides  methods for string representation,
    and arithmetic and comparison operators
    """

    units = MappingProxyType({

                    "degreeminutesecond":
                        {
                            "name": "degreeminutesecond",
                            "toseconds": lambda dms: (dms[0] * 3600) + (dms[1] * 60) + (dms[2]),
                            "fromseconds": lambda s: (s // 3600, (s - ((s // 3600)*3600))//60, s - ((s // 3600)*3600) - (((s - ((s // 3600)*3600))//60)*60)),
                            "tostring": lambda v: f"{v[0]}° {v[1]}′ {v[2]}″"
                        },

                    "radian":
                        {
                            "name": "radian",
                            "toseconds": lambda r: r * ((180 / math.pi) * 3600),
                            "fromseconds": lambda s: (s / 3600) / (180 / math.pi),
                            "tostring": lambda v: f"{v} rad"
                        },

                    "gradian":
                        {
                            "name": "gradian",
                            "toseconds": lambda g: g * 3240,
                            "fromseconds": lambda s: s / 3240,
                            "tostring": lambda v: f"{v} gon"
                        },

                    "turn":
                        {
                            "name": "turn",
                            "toseconds": lambda t: t * 1296000,
                            "fromseconds": lambda s: s / 1296000,
                            "tostring": lambda v: f"{v} tr"
                        },

                    "hourangle":
                        {
                            "name": "hourangle",
                            "toseconds": lambda ha: ha * 54000,
                            "fromseconds": lambda s: s / 54000,
                            "tostring": lambda v: f"{v} ha"
                        },

                    "point":
                        {
                            "name": "point",
                            "toseconds": lambda p: p * 40500,
                            "fromseconds": lambda s: s / 40500,
                            "tostring": lambda v: f"{v} pt"
                        },

                    "quadrant":
                        {
                            "name": "quadrant",
                            "toseconds": lambda q: q * 324000,
                            "fromseconds": lambda s: s / 324000,
                            "tostring": lambda v: f"{v} quad"
                        }

               })


    def __init__(self, value = 0, unit = units["degreeminutesecond"]):

        self.seconds = unit["toseconds"](value)
        self.unit = unit


    @property
    def value(self):
        return self.unit["fromseconds"](self.seconds)


    @value.setter
    def value(self, value):

        self.seconds = self.unit["toseconds"](value)


    def __str__(self):

        value = self.unit['fromseconds'](self.seconds)
        
        return f"{self.unit['tostring'](value)}"


    def approx_equal(self, other):

        return math.isclose(self.seconds, other.seconds)

    
    # arithmetic methods


    def __add__(self, other):

        seconds = self.seconds + other.seconds
        value = self.unit['fromseconds'](seconds)

        return Angle(value, self.unit)


    def __sub__(self, other):

        seconds = self.seconds - other.seconds
        value = self.unit['fromseconds'](seconds)

        return Angle(value, self.unit)


    def __mul__(self, value):

        seconds = self.seconds * value
        value = self.unit['fromseconds'](seconds)

        return Angle(value, self.unit)


    def __rmul__(self, value):
        
        seconds = value * self.seconds
        value = self.unit['fromseconds'](seconds)

        return Angle(value, self.unit)


    def __truediv__(self, value):
        
        seconds = self.seconds / value
        value = self.unit['fromseconds'](seconds)

        return Angle(value, self.unit)

    
    # comparison methods


    def __lt__(self, other):

        return self.seconds < other.seconds


    def __le__(self, other):

        return self.seconds <= other.seconds


    def __eq__(self, other):

        return self.seconds == other.seconds


    def __gt__(self, other):

        return self.seconds > other.seconds


    def __ge__(self, other):

        return self.seconds >= other.seconds


    def __ne__(self, other):

        return self.seconds != other.seconds



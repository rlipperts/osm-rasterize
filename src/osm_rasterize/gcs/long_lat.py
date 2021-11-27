import numbers

from osm_rasterize.gcs.error import InvalidCoordinateError, GeographyError
from osm_rasterize.gcs.math import ring_addition


class Itude(float):
    """
    Upper Class for Latitude and Longitude.
    Contains general logic for both classes.
    """

    _value: float

    lower_limit: int
    upper_limit: int

    # todo: theoretically it still is possible to get subclasses higher than the limit (
    #  multiplication, etc.)

    def __new__(cls, value):
        return float.__new__(cls, value)

    def __init__(self, value: numbers.Number):
        self.value = value

    def __add__(self, other):
        return self._create(self._add(other))

    def __radd__(self, other):
        return self._create(self._add(other))

    def __iadd__(self, other):
        self.value = self._add(other)

    def __ge__(self, other):
        return self.value >= other

    def _add(self, other):
        try:
            if isinstance(other, Itude) and self.__class__ != other.__class__:
                raise GeographyError('Cannot calculate sum out of Latitude and Longitude!')
            return ring_addition(self._value, other, self.upper_limit, self.lower_limit)
        except AttributeError:
            return ring_addition(self._value, other.value, self.upper_limit, self.lower_limit)

    @classmethod
    def _create(cls, value):
        return cls(value)

    @property  # type: ignore
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        try:  # todo: abc does not work if there are no abstract methods
            if abs(value) > self.upper_limit:
                raise InvalidCoordinateError(
                    f'Value must be between {self.lower_limit} and {self.upper_limit}!')
            self._value = value
        except AttributeError as error:
            raise NotImplementedError('Cannot instantiate abstract class!') from error


class Latitude(Itude):
    """
    Latitude units.
    Cannot exceed 90 in the positive or negative.
    """
    lower_limit = -90
    upper_limit = 90


class Longitude(Itude):
    """
    Latitude units.
    Cannot exceed 180 in the positive or negative.
    """
    lower_limit = -180
    upper_limit = 180

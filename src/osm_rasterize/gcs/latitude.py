from dataclasses import dataclass, field

from osm_rasterize.gcs.errors import InvalidLatitudeError
from osm_rasterize.gcs.math import ring_addition


@dataclass
class Latitude:
    """
    Latitude units.
    Cannot exceed 180 in the positive or negative.
    """

    # todo: merge latitude and longitude in a parent class
    lower_limit = -90
    upper_limit = 90

    # if you are confused by the double declaration here read this:
    # https://florimond.dev/en/posts/2018/10/reconciling-dataclasses-and-properties-in-python/
    latitude: float
    _latitude: float = field(init=False, repr=False)

    def __add__(self, other):
        return Latitude(self._add(other))

    def __radd__(self, other):
        return Latitude(self._add(other))

    def __iadd__(self, other):
        self.latitude = self._add(other)

    def __ge__(self, other):
        return self.latitude >= other

    def _add(self, other):
        return ring_addition(self._latitude, other, self.upper_limit, self.lower_limit)

    @property  # type: ignore
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value: float):
        if abs(value) > self.upper_limit:
            raise InvalidLatitudeError('Latitude must be between -90 and 90!')
        self._latitude = value

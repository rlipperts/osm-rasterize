from dataclasses import field, dataclass

from osm_rasterize.gcs.errors import InvalidLongitudeError
from osm_rasterize.gcs.math import ring_addition


@dataclass
class Longitude:
    """
    Longitude units.
    Cannot exceed 180 in the positive or negative.
    """

    # todo: merge longitude and longitude in a parent class
    lower_limit = -180
    upper_limit = 180

    # if you are confused by the double declaration here read this:
    # https://florimond.dev/en/posts/2018/10/reconciling-dataclasses-and-properties-in-python/
    longitude: float
    _longitude: float = field(init=False, repr=False)

    def __add__(self, other):
        return Longitude(self._add(other))

    def __radd__(self, other):
        return Longitude(self._add(other))

    def __iadd__(self, other):
        self.longitude = self._add(other)

    def __ge__(self, other):
        return self.longitude >= other

    def _add(self, other):
        return ring_addition(self._longitude, other, self.upper_limit, self.lower_limit)

    @property  # type: ignore
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value: float):
        if abs(value) > self.upper_limit:
            raise InvalidLongitudeError('Longitude must be between -90 and 90!')
        self._longitude = value

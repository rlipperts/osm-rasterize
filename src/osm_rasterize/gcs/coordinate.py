from osm_rasterize.gcs.longitude import Longitude
from osm_rasterize.gcs.latitude import Latitude


class Coordinate:

    def __init__(self, lat: Latitude, long: Longitude):
        self._lat = lat
        self._long = long

    @classmethod
    def from_xy_coordinates(cls, x: int, y: int):  # pylint: disable=invalid-name
        # todo: implement me!
        pass

    def to_xy_coordinates(self) -> tuple[int, int]:
        # todo: implement me!
        pass

    @property
    def latitude(self):
        return self._lat.latitude

    @latitude.setter
    def latitude(self, value: float):
        self._lat.latitude = value

    @property
    def longitude(self):
        return self._long.longitude

    @longitude.setter
    def longitude(self, value: float):
        self._long.longitude = value

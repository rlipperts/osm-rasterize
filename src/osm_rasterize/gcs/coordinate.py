from typing import TypedDict

from osm_rasterize.gcs.long_lat import Longitude
from osm_rasterize.gcs.long_lat import Latitude


class RawCoordinate(TypedDict):
    lat: float
    lon: float


class Coordinate:

    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_float(cls, lat: float, long: float):
        return cls(Latitude(lat), Longitude(long))

    @classmethod
    def from_raw(cls, raw: RawCoordinate):
        return cls.from_float(raw['lat'], raw['lon'])

    @classmethod
    def from_xy_coordinates(cls, x: int, y: int):  # pylint: disable=invalid-name
        # todo: implement me!
        pass

    def to_xy_coordinates(self) -> tuple[int, int]:
        # todo: implement me!
        pass

import math

from osm_rasterize.gcs.errors import InvalidBoundsError
from osm_rasterize.gcs.latitude import Latitude
from osm_rasterize.gcs.longitude import Longitude
from osm_rasterize.gcs.coordinate import Coordinate


class BoundingBox:

    def __init__(self, south: Latitude, west: Longitude, north: Latitude, east: Longitude):
        if south >= north or west >= east:
            raise InvalidBoundsError('BoundingBox area is zero or negative, it must be positive!')

        self.south = south
        self.west = west
        self.north = north
        self.east = east

    @classmethod
    def from_floats(cls, south: float, west: float, north: float, east: float):
        return cls(Latitude(south), Longitude(west), Latitude(north), Longitude(east))

    @classmethod
    def from_list(cls, bbox: list[float]):
        return cls.from_floats(*bbox)

    @classmethod
    def around_center(cls, center: Coordinate, radius_in_meters: int):
        return cls(
            center.latitude - radius_in_meters / 111111,
            center.longitude - radius_in_meters / (111111 * math.cos(center.latitude)),
            center.latitude + radius_in_meters / 111111,
            center.longitude + radius_in_meters / (111111 * math.cos(center.latitude))
        )

    @classmethod
    def between_coordinats(cls, coordinate_a: Coordinate, coordinate_b: Coordinate):
        pass

    @staticmethod
    def _meter_to_lat(meters: int):
        return meters / 111111

    @staticmethod
    def _meter_to_long(meters: int, lat: Latitude):
        return meters / (111111 * math.cos(lat.latitude))

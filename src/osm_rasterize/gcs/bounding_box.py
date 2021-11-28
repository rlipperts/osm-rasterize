import math
from typing import TypedDict

from osm_rasterize.gcs.error import InvalidBoundsError
from osm_rasterize.gcs.long_lat import Latitude, Longitude
from osm_rasterize.gcs.coordinate import Coordinate


class RawBoundingBox(TypedDict):
    minlat: float
    minlon: float
    maxlat: float
    maxlon: float


class BoundingBox:
    south: Latitude
    west: Longitude
    north: Latitude
    east: Longitude

    def __init__(self, south: Latitude, west: Longitude, north: Latitude, east: Longitude):
        if south >= north or west >= east:
            raise InvalidBoundsError('BoundingBox area is zero or negative, it must be positive!')

        self.south = south
        self.west = west
        self.north = north
        self.east = east

    def __str__(self):
        return f'BoundingBox(south={self.south}, west={self.west}, north={self.north}, ' \
               f'east={self.east})'

    def __repr__(self):
        return str(self)

    @classmethod
    def from_floats(cls, south: float, west: float, north: float, east: float):
        return cls(Latitude(south), Longitude(west), Latitude(north), Longitude(east))

    @classmethod
    def from_raw(cls, raw: RawBoundingBox):
        return cls.from_floats(raw['minlat'], raw['minlon'], raw['maxlat'], raw['maxlon'])

    @classmethod
    def around_center(cls, center: Coordinate, radius_in_meters: int):
        # noinspection PyTypeChecker
        return cls(
            center.latitude - cls._meter_to_lat(radius_in_meters),
            center.longitude - cls._meter_to_long(radius_in_meters, center.latitude),
            center.latitude + cls._meter_to_lat(radius_in_meters),
            center.longitude + cls._meter_to_long(radius_in_meters, center.latitude)
        )

    @classmethod
    def between_coordinates(cls, coordinate_a: Coordinate, coordinate_b: Coordinate):
        if coordinate_a.latitude < coordinate_b.latitude:
            south = coordinate_a.latitude
            north = coordinate_b.latitude
        else:
            north = coordinate_a.latitude
            south = coordinate_b.latitude
        if coordinate_a.longitude < coordinate_b.longitude:
            west = coordinate_a.longitude
            east = coordinate_b.longitude
        else:
            east = coordinate_a.longitude
            west = coordinate_b.longitude
        return cls(south, west, north, east)

    @staticmethod
    def _meter_to_lat(meters: float) -> Latitude:
        # todo these transformations should have their own separate class
        return Latitude(meters / 111111)

    @staticmethod
    def _meter_to_long(meters: float, lat: Latitude) -> Longitude:
        return Longitude(meters / (111111 * math.cos(lat)))

    @property
    def height(self):
        return self.north - self.south

    @property
    def width(self):
        return self.east - self.west

    @property
    def overpass_bbox(self):
        return f'[bbox:{self.south},{self.west},{self.north},{self.east}]'

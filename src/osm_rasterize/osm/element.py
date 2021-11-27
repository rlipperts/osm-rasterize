from dataclasses import dataclass
from enum import Enum
from typing import TypedDict

from osm_rasterize.gcs.bounding_box import BoundingBox, RawBoundingBox
from osm_rasterize.gcs.coordinate import Coordinate, RawCoordinate
from osm_rasterize.osm.error import DataDecodeError


class DataType(Enum):
    NODE = 'node'
    WAY = 'way'
    RELATION = 'relation'


class RawElement(TypedDict):
    type: str
    id: int  # pylint: disable=invalid-name
    bounds: RawBoundingBox
    nodes: list[int]
    lat: float
    lon: float
    geometry: list[RawCoordinate]
    tags: dict[str, str]


@dataclass
class Element:
    type: DataType
    id: int  # pylint: disable=invalid-name
    bounds: BoundingBox
    nodes: list[int]
    geometry: list[Coordinate]
    tags: dict[str, str]

    @classmethod
    def from_raw(cls, raw: RawElement):
        try:
            # nodes are built somewhat different
            if raw['type'] == 'node':
                geometry = [Coordinate.from_float(raw['lat'], raw['lon'])]
            else:
                geometry = [Coordinate.from_raw(raw_coordinate)
                            for raw_coordinate in raw['geometry']]

            return cls(
                DataType(raw['type']),
                raw['id'],
                BoundingBox.from_raw(raw['bounds']),
                raw['nodes'],
                geometry,
                raw['tags']
            )

        # catch all errors and raise a more general error from it
        except Exception as error:
            raise DataDecodeError('Could not load raw data into Object structure!') from error

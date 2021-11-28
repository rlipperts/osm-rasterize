import pytest

from osm_rasterize.gcs.coordinate import Coordinate
from osm_rasterize.gcs.error import InvalidBoundsError
from osm_rasterize.gcs.long_lat import Latitude, Longitude

from osm_rasterize.gcs.bounding_box import BoundingBox


def test_creation():
    assert isinstance(BoundingBox(Latitude(20), Longitude(20), Latitude(30), Longitude(30)),
                      BoundingBox)


def test_creation_with_negative_area_raises():
    with pytest.raises(InvalidBoundsError):
        BoundingBox(Latitude(30), Longitude(30), Latitude(20), Longitude(20))


def test_creation_with_zero_area_raises():
    with pytest.raises(InvalidBoundsError):
        BoundingBox(Latitude(30), Longitude(30), Latitude(30), Longitude(20))


def test_creation_from_float():
    assert isinstance(BoundingBox.from_floats(20.5, 20.5, 30, 21), BoundingBox)


def test_creation_from_raw():
    raw = {
        'minlat': 52.0086455,
        'minlon': 8.516863,
        'maxlat': 52.0098529,
        'maxlon': 8.5183632
    }
    bbox = BoundingBox.from_raw(raw)
    assert bbox.south == raw['minlat']
    assert bbox.west == raw['minlon']
    assert bbox.north == raw['maxlat']
    assert bbox.east == raw['maxlon']


def test_creation_around_center():
    bbox = BoundingBox.around_center(Coordinate.from_float(0, 0), 111111)
    assert bbox.south == -1
    assert bbox.west == -1
    assert bbox.north == 1
    assert bbox.east == 1


@pytest.mark.parametrize('coordinate_a,coordinate_b,expected_south,expected_west,expected_north,'
                         'expected_east',
                         [
                             (Coordinate.from_float(0, 0), Coordinate.from_float(1, 1), 0, 0, 1, 1),
                             (Coordinate.from_float(1, 1), Coordinate.from_float(0, 0), 0, 0, 1, 1),
                             (Coordinate.from_float(1, 0), Coordinate.from_float(0, 1), 0, 0, 1, 1),
                             (Coordinate.from_float(0, 1), Coordinate.from_float(1, 0), 0, 0, 1, 1),
                         ])
def test_creation_between_coordinates(coordinate_a, coordinate_b, expected_south, expected_west,
                                      expected_north, expected_east):
    bbox = BoundingBox.between_coordinates(coordinate_a, coordinate_b)
    assert bbox.south == expected_south
    assert bbox.west == expected_west
    assert bbox.north == expected_north
    assert bbox.east == expected_east


def test_creation_between_similar_coordinates():
    with pytest.raises(InvalidBoundsError):
        coord = Coordinate.from_float(0, 0)
        BoundingBox.between_coordinates(coord, coord)


def test_height():
    assert BoundingBox(Latitude(20), Longitude(20), Latitude(30), Longitude(30)).height == 10


def test_width():
    assert BoundingBox(Latitude(20), Longitude(20), Latitude(30), Longitude(30)).width == 10

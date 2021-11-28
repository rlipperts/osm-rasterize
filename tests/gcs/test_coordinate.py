import pytest

from osm_rasterize.gcs.error import GeographyError
from osm_rasterize.gcs.long_lat import Longitude, Latitude

from osm_rasterize.gcs.coordinate import Coordinate


def test_valid_creation():
    assert isinstance(Coordinate(Latitude(20), Longitude(20)), Coordinate)


def test_invalid_creation():
    with pytest.raises(GeographyError):
        Coordinate(Latitude(1000), Longitude(20))


def test_valid_float_creation():
    assert isinstance(Coordinate.from_float(20.1234, 30.4312), Coordinate)


def test_invalid_float_creation():
    with pytest.raises(GeographyError):
        Coordinate.from_float(2000.1234, 30.4312)


def test_valid_raw_creation():
    assert isinstance(Coordinate.from_raw({"lat": 20.1234, "lon": 30.4312}), Coordinate)


def test_invalid_raw_creation():
    with pytest.raises(GeographyError):
        Coordinate.from_raw({"lat": 2000.1234, "lon": 30.4312})

import pytest

from osm_rasterize.gcs.error import InvalidCoordinateError, GeographyError
from osm_rasterize.gcs.long_lat import Latitude, Longitude, Itude


def test_lat_creation():
    Latitude(20)


def test_long_creation():
    Longitude(20)


def test_parent_class_abstract():
    with pytest.raises(NotImplementedError):
        Itude(0)


@pytest.mark.parametrize('limit', [-91, 91])
def test_lat_limit(limit):
    with pytest.raises(InvalidCoordinateError):
        Latitude(limit)


@pytest.mark.parametrize('limit', [-181, 181])
def test_long_limit(limit):
    with pytest.raises(InvalidCoordinateError):
        Longitude(limit)


def test_number_addition():
    result = Latitude(20) + 20
    assert isinstance(result, Latitude)
    assert result.value == 40


def test_right_addition():
    result = 20 + Latitude(20)
    assert isinstance(result, Latitude)
    assert result.value == 40


def test_class_addition():
    result = Latitude(20) + Latitude(20)
    assert isinstance(result, Latitude)
    assert result.value == 40


def test_cross_addition():
    with pytest.raises(GeographyError):
        Latitude(20) + Longitude(20)


def test_overflow_addition():
    assert Latitude(90) + 10 == -80

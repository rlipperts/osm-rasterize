import pytest


from osm_rasterize.gcs.longitude import Longitude
from osm_rasterize.gcs.errors import InvalidLongitudeError


def test_creation():
    Longitude(10)


def test_invalid_creation():
    with pytest.raises(InvalidLongitudeError):
        Longitude(181)


def test_addition():
    assert (Longitude(10) + 10).longitude == 20


def test_overflow_addition():
    assert (Longitude(180) + 10).longitude == -170

import pytest


from osm_rasterize.gcs.latitude import Latitude
from osm_rasterize.gcs.errors import InvalidLatitudeError


def test_creation():
    Latitude(10)


def test_invalid_creation():
    with pytest.raises(InvalidLatitudeError):
        Latitude(91)


def test_addition():
    assert (Latitude(10) + 10).latitude == 20


def test_overflow_addition():
    assert (Latitude(90) + 10).latitude == -80

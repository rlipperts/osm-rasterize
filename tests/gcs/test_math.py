import pytest

from osm_rasterize.gcs import math


@pytest.mark.parametrize('summand_a,summand_b,upper_limit,lower_limit,expected_result',
                         [
                             (-100, 30, 180, -180, -70),
                             (-100, 130, 180, -180, 30),
                             (100, 100, 180, -180, -160),
                             (-100, -90, 180, -180, 170),
                             (-200, 90, -180, -360, -290),
                             (-200, -200, -180, -360, -220),
                             (400, 20, 720, 360, 420),
                         ])
def test_ring_addition(summand_a, summand_b, upper_limit, lower_limit, expected_result):
    assert math.ring_addition(summand_a, summand_b, upper_limit, lower_limit) == expected_result


@pytest.mark.parametrize('minuend,subtrahend,upper_limit,lower_limit,expected_result',
                         [
                             (-100, 30, 180, -180, -130),
                             (100, 130, 180, -180, -30),
                             (-100, 100, 180, -180, 160),
                             (100, -90, 180, -180, -170),
                             (-200, -90, -180, -360, -290),
                             (-200, 200, -180, -360, -220),
                             (400, 20, 720, 360, 380),
                         ])
def test_ring_subtraction(minuend, subtrahend, upper_limit, lower_limit, expected_result):
    assert math.ring_subtraction(minuend, subtrahend, upper_limit, lower_limit) == expected_result

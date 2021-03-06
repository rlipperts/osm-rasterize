from osm_rasterize.gcs.error import InvalidBoundsError


def ring_addition(summand_a, summand_b, upper_limit, lower_limit=0):
    if lower_limit >= upper_limit:
        raise InvalidBoundsError('The ring must be larger than zero!')
    ring_size = upper_limit - lower_limit
    shift = -lower_limit
    return (summand_a + summand_b + shift) % ring_size - shift


def ring_subtraction(minuend, subtrahend, upper_limit, lower_limit=0):
    return ring_addition(minuend, -1 * subtrahend, upper_limit, lower_limit)

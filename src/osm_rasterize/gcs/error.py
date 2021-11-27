class GeographyError(Exception):
    pass


class InvalidCoordinateError(GeographyError):
    pass


class InvalidBoundsError(GeographyError):
    pass

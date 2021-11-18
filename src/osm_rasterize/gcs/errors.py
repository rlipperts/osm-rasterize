class GeographyError(Exception):
    pass


class InvalidLatitudeError(GeographyError):
    pass


class InvalidLongitudeError(GeographyError):
    pass


class InvalidBoundsError(GeographyError):
    pass

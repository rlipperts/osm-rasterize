"""
Implement tests here (and in other files, one for every python module you want to test).
"""
import pytest


@pytest.fixture
def overpass_query():
    # with Path("data/query/full_query.ql").open() as file:
    #     query_str = ''
    #     for line in file.readlines():
    #         query_str += line.strip()
    return '[bbox:41.89088797265867,12.488446980714798,41.89177449419739,12.489861845970154];(' \
           'nwr]["landuse"];nwr["natural"];way["highway"];nwr["railway"];nwr["aeroway"];' \
           'nwr["leisure"];nwr["power"];nwr["military"];relation["place"];nwr["amenity"];' \
           'way["waterway"];node["man-made"];);(._;>;);out;'


def test_main():
    pass

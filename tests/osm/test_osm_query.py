import pytest
from overpy import Overpass, Result


@pytest.fixture
def xml_response() -> str:
    with open('data/query/overpass_query_response.xml') as res:
        return res.read()


@pytest.fixture
def op_query() -> str:
    with open('data/query/full_query.ql') as query:
        return query.read()


@pytest.fixture
def op_api() -> Overpass:
    return Overpass()


@pytest.fixture
def op_response(xml_response: str, op_api: Overpass) -> Result:
    return op_api.parse_xml(xml_response)


def test_overpy_api_response(op_api: Overpass, op_query: str, op_response: Result):
    """ Validate response from the Overpass API.
    """
    result = op_api.query(op_query)
    assert op_response.way_ids == result.way_ids
    assert op_response.node_ids == result.node_ids
    assert op_response.area_ids == result.area_ids

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

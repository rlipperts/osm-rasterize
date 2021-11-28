from overpy import Overpass, Result


def test_overpy_api_response(op_api: Overpass, op_query: str, op_response: Result):
    """ Validate response from the Overpass API.
    """
    result = op_api.query(op_query)
    assert op_response.way_ids == result.way_ids
    assert op_response.node_ids == result.node_ids
    assert op_response.area_ids == result.area_ids

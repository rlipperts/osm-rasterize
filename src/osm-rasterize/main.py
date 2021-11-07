"""
Implement the functionality here (and in sub-packages).
"""
from pathlib import Path

from OSMPythonTools.overpass import Overpass, overpassQueryBuilder


def build_query():
    bounding_box = [52.00957239639684, 8.510826230049133, 52.01387794408706, 8.520970344543457]
    element_type = ['node', 'way', 'relation']
    selector = [
        '"landuse"~""',
        # '"natural"~""',
        # '"railway"~""',
        # '"aeroway"~""',
        # '"leisure"~""',
        # '"power"~""',
        # '"military"~""',
        # '"amenity"~""',
        # '"highway"~""',
        # '"waterway"~""',
        # '"place"~""',
        # '"man-made"~""',
    ]
    # https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_.28.3E.29
    # https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Sets
    # https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out
    query = overpassQueryBuilder(
        bbox=bounding_box,
        elementType=element_type,
        selector=selector,
        out='body',
        includeGeometry=True,
    )
    return query


def build_queries():
    # https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_.28.3E.29
    # https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Sets
    # https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out
    bounding_box = [52.00957239639684, 8.510826230049133, 52.01387794408706, 8.520970344543457]
    queries = {
        'building': ['node', 'way', 'relation'],
        'landuse': ['node', 'way', 'relation'],
        'natural': ['node', 'way', 'relation'],
        'railway': ['node', 'way', 'relation'],
        'aeroway': ['node', 'way', 'relation'],
        'leisure': ['node', 'way', 'relation'],
        'power': ['node', 'way', 'relation'],
        'military': ['node', 'way', 'relation'],
        'amenity': ['node', 'way', 'relation'],
        'place': 'relation',
        'highway': 'way',
        'waterway': 'way',
        'man-made': 'node',
    }
    return {
        selector: overpassQueryBuilder(
            bbox=bounding_box,
            elementType=element_type,
            selector=f'\'"{selector}"~""\'',
            out='body',
            includeGeometry=True,
        )
        for selector, element_type in queries.items()
    }


overpass = Overpass()
queries = build_queries()
results = {selector: overpass.query(query) for selector, query in queries.items()}

out_dir = Path.cwd() / 'out'
out_dir.mkdir(exist_ok=True)
for selector, result in results.items():
    with open(out_dir / f'{selector}.json', mode='w') as file:
        file.write(str(result.toJSON()))

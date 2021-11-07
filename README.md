# osm rasterize
_Transform OSM environment data into a grid_

## installation
There are no PyPI releases. Neither are they planned.

### manual
For installation with pip directly from this GitHub repository simply open a terminal and type
```
pip install git+ssh://git@github.com/rlipperts/osm-rasterize.git
``` 

### setup.py
To automatically install the logging configurator with your python package include these lines in your setup.py
```python
install_requires = [
    'osm-rasterize @ git+ssh://git@github.com/rlipperts/osm-rasterize.
                       git@master#egg=osm-rasterize-0.0.0',
],
```
Make sure you update the version in the `egg=osm-rasterize-...` portion to the correct version 
specified in the logging-configurators setup.py. This might not work if you plan on publishing your package on PyPI.

## usage

1. Spiellogik und -grafik
2. Spielweltgenerierung
3. __Echtwelt Datenaufarbeitung__

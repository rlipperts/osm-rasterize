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
    'osm_rasterize @ git+ssh://git@github.com/rlipperts/osm_rasterize.
                       git@master#egg=osm_rasterize-0.0.0',
],
```
Make sure you update the version in the `egg=osm-rasterize-...` portion to the correct version 
specified in the logging-configurators setup.py. This might not work if you plan on publishing your package on PyPI.

## Overview

1. Spiellogik und -grafik
2. Spielweltgenerierung
3. __Echtwelt Datenaufarbeitung__

## Link Dump

* Map Transformations
    * [Geodesic Grid as alternative to square-based representations?](https://en.wikipedia.org/wiki/Geodesic_grid)
    * [Better square mapping](https://en.wikipedia.org/wiki/Quadrilateralized_spherical_cube)
* Tools
    * [Tile Map Editor](https://www.mapeditor.org/)
    * [Overpass Query online interpreter](https://overpass-turbo.eu/)
* Ressources
    * [Tuxemon - open source tiles and pokemon](https://github.com/Tuxemon/Tuxemon/tree/development/mods/tuxemon/gfx/tilesets)

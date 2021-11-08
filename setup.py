import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

test_deps = [
    'pytest',
    'flake8',
    'pylint',
    'mypy',
]
extras = {
    'test': test_deps
}

setuptools.setup(
    name="osm_rasterize",
    version="0.0.0",
    author="Ruben Lipperts",
    author_email="",
    description="Map OSM data onto a grid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlipperts/osm-rasterize",
    package_dir={'': 'src'},
    packages=['osm_rasterize'],
    package_data={'osm_rasterize': ['py.typed']},
    tests_require=test_deps,
    extras_require=extras,
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
    ],
    python_requires='~=3.9',
)

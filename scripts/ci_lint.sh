#!/bin/bash
flake8
pylint src
pylint scripts
mypy src
mypy scripts
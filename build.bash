#!/bin/bash

rm -r dist
pip uninstall clime_bus_factor -y
python -m build
pip install dist/clime_*

echo
echo "Done building"

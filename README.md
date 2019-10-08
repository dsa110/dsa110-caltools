# dsa110-caltools
Functions for finding calibrators for DSA-110

# Installation

> python setup.py install

# Usage

> from caltools import caltools
> cats = caltools.list_calibrators(180., 50.)
> print(cats.keys())
['FIRST', 'NVSS']

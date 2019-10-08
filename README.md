# dsa110-caltools
Functions for finding calibrators for DSA-110

# Installation

Clone dsa110-caltools, then:
```
> python setup.py install
```

# Usage

```
> from caltools import caltools
> cats = caltools.list_calibrators(180., 50.)
> print(cats.keys())
dict_keys(['FIRST', 'NVSS'])
```

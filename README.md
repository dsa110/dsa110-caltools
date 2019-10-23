# dsa110-caltools
Functions for finding calibrators for DSA-110

# Installation

Clone dsa110-caltools, then:
```
> python setup.py install
```
or
```
pip install https+git://github.com/dsa110/dsa110-caltools.git
```

# Usage

```
> from caltools import caltools
> tab = caltools.list_calibrators(202.78333, 30.50889, surveys=['NVSS'], radius=0.1)
> print(tab['NVSS'])
        NAME            ra      dec       flux         separation    
                       deg      deg       MJY                        
------------------- --------- -------- ---------- -------------------
NVSS J133108+303032 202.78463 30.50900    14902.7 0.06752421825348585
NVSS J133113+302630 202.80675 30.44172       21.3   4.208229887846443
```

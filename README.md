# dsa110-catalogs
Functions for using catalogs of calibrators and sources for DSA-110

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
> from catalogs import caltools
> tab = caltools.list_calibrators(202.78333, 30.50889, surveys=['NVSS'], radius=0.1)
> print(tab['NVSS'])
        NAME            ra      dec       flux         separation    
                       deg      deg       MJY                        
------------------- --------- -------- ---------- -------------------
NVSS J133108+303032 202.78463 30.50900    14902.7 0.06752421825348585
NVSS J133113+302630 202.80675 30.44172       21.3   4.208229887846443
```

and

```
> from catalogs import astrometry
> from astropy import coordinates, units
> cat = astrometry.VLASSCat()  # default catalog path works on h23
> cat.search(coordinates.SkyCoord(0, 0, unit=units.deg), halfwidth=10*units.arcmin)
                     source_name        RA       DEC  Total_flux  Peak_flux  ...       Min     E_Min          PA       E_PA  S_Code
693813  T11t01_J000200+003000_39  0.154320  0.100989    0.001878   0.001859  ...  0.000642  0.000061  119.515541  31.073290       S
693819  T11t01_J000200+003000_45  0.048381  0.061214    0.004813   0.003966  ...  0.000668  0.000038  159.488230  11.810685       S

[2 rows x 12 columns]
```
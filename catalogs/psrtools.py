"""Functions to look up pulsar catalogs.
"""

import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from psrqpy import QueryATNF

QUERY = QueryATNF(params=['DM', 'RAJ', 'DECJ', 'S1400', 'PSRJ', 'PSRB'])

def match_pulsar(RA_mjd, Dec_mjd, thresh_deg=3.5):
    """Determine if a pulsar is close to a given ra, dec.
    """
    RA_psr, Dec_psr, _DM = np.array(QUERY['RAJ']), np.array(QUERY['DECJ']), np.array(QUERY['DM'])
#    print(RA_mjd, Dec_mjd)
    _coord = SkyCoord(ra=RA_mjd, dec=Dec_mjd)
    catalog = SkyCoord(ra=RA_psr, dec=Dec_psr, unit=(u.h, u.deg))

    ra, dec = catalog.data.lon.deg, catalog.data.lat.value
    sep_deg = np.sqrt((ra-RA_mjd.value)**2 + (dec - Dec_mjd.value)**2)
    ind_near = np.where(sep_deg < thresh_deg)[0]
    #idx, d2, d3 = c.match_to_catalog_sky(catalog)

    return ind_near

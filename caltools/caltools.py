# Functions heavily borrowed from rf_meta_query/catalog_utils.py by X Prochaska
# claw, 19oct07

from __future__ import print_function, division, absolute_import, unicode_literals
from builtins import bytes, dict, object, range, map, input, str
from future.utils import itervalues, viewitems, iteritems, listvalues, listitems
from io import open

import numpy as np
from astropy import coordinates, units
from astroquery.heasarc import Heasarc

heasarc = Heasarc()


def list_calibrators(ra, dec, surveys=["FIRST", "NVSS"], radius=2*units.deg):
    """ Search surveys for sources near (ra, dec)
    Args:
        ra, dec: float
          Coordinates in degrees
        surveys: list(str)
          Survey strings used by HEASARC
        radius: astropy.units
    """
    
    tables = {}
    coord = coordinates.SkyCoord(ra=ra, dec=dec, unit=(units.deg, units.deg))

    for survey in surveys:
        cat = query_heasarc(coord=coord, mission=survey, radius=radius)
        if cat is not None:
            cat = sort_by_separation(clean_heasarc(cat), coord=coord)
            if 'FLUX_20_CM' in cat.columns:
                cat.rename_column("FLUX_20_CM", "flux")
                cols_keep = ['NAME', 'ra', 'dec', 'flux', 'separation']
            else:
                cols_keep = ['NAME', 'ra', 'dec', 'separation']
            tables[survey] = cat[cols_keep]

    return tables


def query_heasarc(coord=None, ra=None, dec=None, mission='FIRST', radius=2*units.deg):
    """
    Use astroquery to query the HEARSARC database

    Args:
        ra, dec: float (degrees)
        coord: astropy.coordinates.sky_coordinate.SkyCoord
        mission: str
          Uses HEASARC notation
        radius: Angle

    Returns:
    """

    if ra is not None and dec is not None:
        coord = coordinates.SkyCoord(ra=ra, dec=dec, unit=(units.deg, units.deg))

    assert isinstance(coord, coordinates.sky_coordinate.SkyCoord)

    catalog = None
    try:
        catalog = heasarc.query_region(coord, mission=mission, radius=radius)
    except (ValueError, TypeError):
        logger.warn("No source found at {0}".format(coord))

    return catalog


def sort_by_separation(catalog, coord, radec=('ra', 'dec'), add_sep=True):
    """
    Sort an input catalog by separation from input coordinate

    Args:
        catalog: astropy.table.Table
        coord: SkyCoord
        radec: tuple
          Defines catalog columns holding RA, DEC (in deg)
        add_sep: bool, optional
          Add a 'separation' column with units of arcmin

    Returns:
        srt_catalog: astropy.table.Table
          Sorted catalog

    """
    # Check
    for key in radec:
        if key not in catalog.keys():
            print("RA/DEC key: {:s} not in your Table".format(key))
            raise IOError("Try again..")
    # Grab coords
    cat_coords = coordinates.SkyCoord(ra=catalog[radec[0]].data,
                                      dec=catalog[radec[1]].data, unit='deg')

    # Separations
    seps = coord.separation(cat_coords)
    isrt = np.argsort(seps)
    # Add?
    if add_sep:
        catalog['separation'] = seps.to('arcmin').value
    # Sort
    srt_catalog = catalog[isrt]
    # Return
    return srt_catalog


def clean_heasarc(catalog):
    """ Renames columns
    """

    catalog.rename_column("RA", "ra")
    catalog.rename_column("DEC", "dec")
    for key in ['ra', 'dec']:
        catalog[key].unit = units.deg

    return catalog

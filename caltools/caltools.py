# Functions heavily borrowed from rf_meta_query/catalog_utils.py by X Prochaska
# claw, 19oct07

import numpy as np
from astropy import coordinates, units
from astroquery.heasarc import Heasarc
import logging
logging.basicConfig(format='%(asctime)s %(message)s')

heasarc = Heasarc()

_beamradius_DSA = 2.


def get_calibrator_lists(ra, dec, fluxratio=0.7, survey='NVSS', radius=_beamradius_DSA):
    """ Given ra,dec, define list of calibrator sources that includes fluxratio of the total flux in the field.
    Returns array of tuples (ra, dec, flux) to be used as input to models.
    Can optionally define survey and radius for catalog query.
    """

    table = list_calibrators(ra, dec, surveys=[survey], radius=radius)[survey]
    if table is None:
        return np.empty(0)

    table.sort(keys='flux', reverse=True)
    totalflux = table['flux'].sum()  # TODO: define as all flux but select on compact sources?
    if fluxratio < 1:
        ind = np.where(np.cumsum(table['flux']) > fluxratio*totalflux)[0][0] + 1
    else:
        ind = len(table)

    return np.array(table[:ind]['ra', 'dec', 'flux'])


def list_calibrators(ra, dec, surveys=["NVSS"], radius=_beamradius_DSA):
    """ Search surveys for sources near (ra, dec)
    Args:
        ra, dec: float
          Coordinates in degrees
        surveys: list(str)
          Survey strings used by HEASARC (e.g., FIRST, NVSS)
        radius: float
          Radius of aree to include in degrees
    """
    
    tables = {}
    coord = coordinates.SkyCoord(ra=ra, dec=dec, unit=(units.deg, units.deg))

    for survey in surveys:
        cat = query_heasarc(coord=coord, mission=survey, radius=radius*units.deg)
        if cat is not None:
            cat = sort_by_separation(clean_heasarc(cat), coord=coord)
            if 'FLUX_20_CM' in cat.columns:
                cat.rename_column("FLUX_20_CM", "flux")
                cols_keep = ['NAME', 'ra', 'dec', 'flux', 'separation']
            else:
                cols_keep = ['NAME', 'ra', 'dec', 'separation']
            tables[survey] = cat[cols_keep]
        else:
            tables[survey] = None

    # TODO: select based on source size
    return tables


def query_heasarc(coord=None, ra=None, dec=None, mission='NVSS', radius=_beamradius_DSA*units.deg):
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
        logging.warn("No source found at {0}".format(coord))

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

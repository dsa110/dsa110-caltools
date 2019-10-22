import pytest
from caltools import caltools


def test_querycoord():
    from astropy import coordinates as co, units as u
    coord = co.SkyCoord(ra=180., dec=0., unit=(u.deg, u.deg))
    table = caltools.query_heasarc(coord=coord, surveys=['NVSS'])
    print(table)
    assert table is not None


def test_queryradec():
    table = caltools.query_heasarc(ra=180., dec=0.)
    print(table)
    assert table is not None


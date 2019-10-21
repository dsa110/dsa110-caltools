import pytest
from caltools import caltools


def test_querycoord():
    table = caltools.query_heasarc(coord=coord)
    assert table is not None


def test_queryradec():
    table = caltools.query_heasarc(ra=ra, dec=dec)
    assert table is not None

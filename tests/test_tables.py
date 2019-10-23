import pytest
from caltools import caltools


def test_nvss():
    table = caltools.list_calibrators(180., 0., surveys=["NVSS"], radius=1.)
    print(table)
    assert table is not None


def test_first():
    table = caltools.list_calibrators(180., 40., surveys=["FIRST"], radius=1.)
    print(table)
    assert table is not None


def test_radius():
    table1 = caltools.list_calibrators(180., 40., surveys=["FIRST"], radius=1.)
    table2 = caltools.list_calibrators(180., 40., surveys=["FIRST"], radius=2.)
    print(table1, table2)
    assert len(table2["FIRST"]) > len(table1["FIRST"])
    

def test_getlist():
    ll = caltools.get_calibrator_lists(180., 40., fluxratio=0.7, survey='NVSS')
    print(ll)
    assert len(ll)


def test_listsize():
    ll1 = caltools.get_calibrator_lists(180., 40., fluxratio=0.7, survey='NVSS')
    ll2 = caltools.get_calibrator_lists(180., 40., fluxratio=0.9, survey='NVSS')
    print(ll1, ll2)
    assert len(ll2) > len(ll1)

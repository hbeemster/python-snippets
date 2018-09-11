#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cheese_shop` package."""

import pytest

from cheese_shop import setup_logging

setup_logging('logging_for_tests.yaml')

from cheese_shop.cheese_slicer import CheeseSlicer


@pytest.fixture
def slicer():
    """return a fresh slicer"""
    return CheeseSlicer()


def test_thickness(slicer):
    """"""
    assert slicer.thickness == 3

    slicer.thickness = 0
    assert 1 == slicer.thickness

    slicer.thickness = 10
    assert 5 == slicer.thickness

    slicer.thickness = 3
    slicer.thickness = 3.4
    assert 3 == slicer.thickness


def test_slicer(slicer):
    """"""
    cheese = 'Beemster'
    slices = slicer.slice(cheese)
    assert 63 == len(slices)

    slicer.thickness = 1
    slices = slicer.slice(cheese)
    assert 31 == len(slices)

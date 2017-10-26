#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Malcolm Ramsay <malramsay64@gmail.com>
#
# Distributed under terms of the MIT license.

"""Testing for the Civilisation simulator."""

import pytest
from hypothesis import given
from hypothesis.strategies import integers

from civ import Player, democracy


def test_player_creation():
    Player('me', 1000)


def test_player():
    p = Player('me', 1000)
    assert p.name == 'me'
    assert p.aggression == 1000


def test_set_name():
    p = Player('me', 1000)
    p.name = 'me_too'
    assert p.name == 'me_too'


def test_set_agression():
    p = Player('me', 1000)
    p.aggression = 100
    assert p.aggression == 100


def test_democracy():
    p = Player('me', 1000)
    assert p.aggression == 1000
    democracy(p)
    assert p.aggression == 998


PLAYER_LIST = [
    Player('Angela Merkel', 3),
    Player('Kim Jong Un', 20),
    Player('Donald Trump', 25),
    Player('Malcolm Turnbull', 2),
]

@pytest.mark.parametrize('player', PLAYER_LIST)
def test_many_democracy(player):
    aggression = player.aggression
    democracy(player)
    assert player.aggression == aggression - 2

@given(integers(min_value=0, max_value=255))
def test_aggression_hyypothesis(aggression):
    p = Player('me', aggression)
    assert p.aggression == aggression

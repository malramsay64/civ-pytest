#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Malcolm Ramsay <malramsay64@gmail.com>
#
# Distributed under terms of the MIT license.

def democracy(player):
    """Apply the democracy trait to all players.

    Args:
        player (Player): Player on which to assign democracy

    The democracy trait reduces the aggression of a player by 2

    """
    player.aggression -= 2

def twitter(player):
    """Apply twitter attribute to player.

    Args:
        player (Player): Player for which to assign twitter

    The twitter attribute doubles the players aggression.

    """
    player.aggression *= 2


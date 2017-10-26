# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Malcolm Ramsay <malramsay64@gmail.com>
#
# Distributed under terms of the MIT license.

cdef class Player(object):
    """A player in the game of civilisation.

    The player class holds all the attributes of the player.

    """
    cpdef public unicode name
    cpdef public unsigned int aggression

    def __init__(self, unicode name, int aggression):
        """

        Args:
            name (str): The name of the player
            aggresssion (int): The aggression for the player

        """
        self.name = name
        self.aggression = aggression


cpdef democracy(object p):
    """Apply the democracy trait to all players.

    Args:
        p (Player): Player on which to assign democracy

    The democracy trait reduces the aggression of a player by 2

    """
    p.aggression = <unsigned int>p.aggression - 2

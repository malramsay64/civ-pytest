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
    cpdef public unsigned char aggression

    def __init__(self, unicode name, int aggression):
        """

        Args:
            name (str): The name of the player
            aggresssion (int): The aggression for the player. Aggressions can
                be a value in the range [0, 255].

        """
        self.name = name
        self.aggression = aggression

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Malcolm Ramsay <malramsay64@gmail.com>
#
# Distributed under terms of the MIT license.

class Player:
    def __init__(self, unicode name, int aggression):
        self.name = name
        self.aggression = aggression


cpdef democracy(object p):
    p.aggression = <unsigned int>p.aggression - 2

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Malcolm Ramsay <malramsay64@gmail.com>
#
# Distributed under terms of the MIT license.

"""Simple Civilisation simulator."""

from civ import Player, democracy

if __name__ == '__main__':
    players = [
        Player('Ghandi', aggression=1),
        Player('Trump', aggression=10)
    ]
    for player in players:
        print(f'Player {player.name} has aggression of {player.aggression}')
        democracy(player)
    for player in players:
        print(f'Player {player.name} has aggression of {player.aggression}')


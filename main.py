# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:04:42 2015

@author: baskiotisn
"""


from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle
from monequipe import teams


team1=teams[0]
if len(teams)>1:
    team2=teams[1]
else:
    team2=team1.copy()
bat= SoccerBattle(team2,team1)
obs=PygletObserver()
obs.set_soccer_battle(bat)
pyglet.app.run()


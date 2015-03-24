# -*- coding: utf-8 -*-



from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle
from monequipe import teams
import pickle

team1=teams[0]
team2=teams[-1]

battle= SoccerBattle(team2,team1)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
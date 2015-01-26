# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:54:25 2015

@author: 3301393
"""
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam 
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
import soccersimulator 
from soccersimulator import SoccerAction,SoccerStrategy

v =Vector2D(3,2) 
u =Vector2D(5,4)
acc =Vector2D(2,2)
tir =Vector2D(5,0)

pos =Vector2D.create_random()
shoot =Vector2D.create_random()

class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        pos = Vector2D.create_random(-5,5)
        shoot = Vector2D.create_random(-5,5)
        return SoccerAction(pos,shoot)
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()


class FonceurStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        if(teamid==1):
            pos = state.ball.position-player.position
            shoot = state.get_goal_center(2)-player.position
            return SoccerAction(pos,shoot)
        else:
            pos = state.ball.position-player.position
            shoot = state.get_goal_center(1)-player.position
            return SoccerAction(pos,shoot)
    def copy(self):
        return FonceurStrategy()
    def create_strategy(self):
        return FonceurStrategy()


team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j2",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j3",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j3",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j4",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j4",FonceurStrategy()))

battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
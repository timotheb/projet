from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import *

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("Neuyer",DirPoint,1,2))
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))

teams =[team1,team2]

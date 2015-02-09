from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import *

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team4=SoccerTeam("team4")
team1.add_player(SoccerPlayer("Neuyer",FonceurStrategy()))
team2.add_player(SoccerPlayer("Ronaldo",FonceurStrategy()))
team2.add_player(SoccerPlayer("1",FonceurStrategy()))
team4.add_player(SoccerPlayer("2",FonceurStrategy()))
team4.add_player(SoccerPlayer("3Neuyer",FonceurStrategy()))
team4.add_player(SoccerPlayer("4Ronaldo",FonceurStrategy()))
team4.add_player(SoccerPlayer("5Neuyer",FonceurStrategy()))
teams =[team1,team2,team4]

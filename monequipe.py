from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import *


team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team3=SoccerTeam("Relegation")
team4=SoccerTeam("Meet Your Maker")
team1.add_player(SoccerPlayer("Neuyer",FonceurStrategy()))
team2.add_player(SoccerPlayer("Ronaldo",FonceurStrategy()))
team2.add_player(SoccerPlayer("Neuyer",Goal()))
team3.add_player(SoccerPlayer("Neuyer",FonceurStrategy()))
team3.add_player(SoccerPlayer("Ronaldo",FonceurStrategy()))
team4.add_player(SoccerPlayer("2",FonceurStrategy()))
team4.add_player(SoccerPlayer("3Neuyer",FonceurStrategy()))
team4.add_player(SoccerPlayer("4Ronaldo",FonceurStrategy()))
team4.add_player(SoccerPlayer("5Neuyer",Goal()))
teams =[team2,team3,team4,team1]

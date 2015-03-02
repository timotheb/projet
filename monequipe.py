from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import *


team1=SoccerTeam("AppleJack")
team2=SoccerTeam("BowTie")
team3=SoccerTeam("Cupcake")
team4=SoccerTeam("Posey")
team1.add_player(SoccerPlayer("Neuyer",TirLucarne()))
team2.add_player(SoccerPlayer("Ronaldo",TirLucarne()))
team2.add_player(SoccerPlayer("Neuyer",Goal()))
team3.add_player(SoccerPlayer("Ronaldo",TirLucarne()))
team3.add_player(SoccerPlayer("Neuyer",Goal()))
team4.add_player(SoccerPlayer("2",FonceurStrategy()))
team4.add_player(SoccerPlayer("3Neuyer",FonceurStrategy()))
team4.add_player(SoccerPlayer("4Ronaldo",FonceurStrategy()))
team4.add_player(SoccerPlayer("5Neuyer",Goal()))
teams =[team2,team3,team4,team1]

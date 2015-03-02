from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import *


team1=SoccerTeam("AppleJack")
team2=SoccerTeam("BowTie")
team3=SoccerTeam("Cupcake")
team4=SoccerTeam("Posey")
team1.add_player(SoccerPlayer("60degres",TirLucarne()))
team2.add_player(SoccerPlayer("Classy",TirLucarne()))
team2.add_player(SoccerPlayer("Handsome",Goal()))
team3.add_player(SoccerPlayer("Vanille",TirLucarne()))
team3.add_player(SoccerPlayer("Chocolat",Goal()))
team4.add_player(SoccerPlayer("Audmars-Piguet",FonceurStrategy()))
team4.add_player(SoccerPlayer("Omega",FonceurStrategy()))
team4.add_player(SoccerPlayer("Cartier",FonceurStrategy()))
team4.add_player(SoccerPlayer("Rolex",Goal()))
teams =[team2,team3,team4,team1]

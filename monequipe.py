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
team2.add_player(SoccerPlayer("Handsome",Goalv2()))
team3.add_player(SoccerPlayer("Vanille",TirLucarne()))
team3.add_player(SoccerPlayer("Chocolat",Goal()))
team4.add_player(SoccerPlayer("Audmars-Piguet",Goal()))
team4.add_player(SoccerPlayer("Omega",FonceurStrategy()))
team4.add_player(SoccerPlayer("Cartier",SelectorStrategy()))
team4.add_player(SoccerPlayer("Rolex",TirLucarne()))
teams =[team4,team4,team2,team1]
teams1=[team4,team4,team2,team1]

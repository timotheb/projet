from soccersimulator import *
from strats import *
from outil import *
import os
import pickle
from apprentissage import gen_feature_simple

list_key=['a','z']
list_strat=[TirLucarne(),Goalv2()]
list_nom=["TirLucarne","Goalv2"]
inter_strat=InteractStrategy(list_key,list_strat,"tent3.2.pkl")

list_key2=['a','e','z','s','q','d']
list_strat2=[TirLucarne(),Goalv2(),DepHaut(),DepBas(),DepGauche(),DepDroite()]
list_nom2=["TirLucarne","Goalv2","Haut","Bas","Gauche","Droite"]
inter_strat2=InteractStrategy(list_key2,list_strat2,"tent3.4.pkl")

team1=SoccerTeam("AppleJack")
team2=SoccerTeam("BowTie")
team3=SoccerTeam("Cupcake")
team4=SoccerTeam("Posey")
team5=SoccerTeam("test1v1")

team1.add_player(SoccerPlayer("60degres",inter_strat2))

team5.add_player(SoccerPlayer("60degres",TirLucarne()))

team2.add_player(SoccerPlayer("Classy",TirLucarne()))
team2.add_player(SoccerPlayer("Handsome",inter_strat2))



team3.add_player(SoccerPlayer("Vanille",TirLucarne()))
team3.add_player(SoccerPlayer("Chocolat",Goal()))

team4.add_player(SoccerPlayer("Audmars-Piguet",Goal()))
team4.add_player(SoccerPlayer("Omega",FonceurStrategy()))
team4.add_player(SoccerPlayer("Cartier",TirLucarne()))
team4.add_player(SoccerPlayer("Rolex",TirLucarne()))


### Apprentissage

team_tree = SoccerTeam("Team Tree")

treeia=TreeIA(gen_feature_simple,dict(zip(list_nom2,list_strat2)))

fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"tree3.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree3",treeia)

team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("Tree 2",TreeST))



teams =[team_tree,team2,team3,team4,team1,team5]
teams1=[team_tree,team2,team3,team4,team1]

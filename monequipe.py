from soccersimulator import *
from strats import *
import os
import pickle
from apprentissage import gen_feature_simple

list_key=['a','z']
list_strat=[TirLucarne(),Goalv2()]
list_nom=["TirLucarne","Goalv2"]
inter_strat=InteractStrategy(list_key,list_strat,"tent3.2.pkl")


team1=SoccerTeam("AppleJack")
team2=SoccerTeam("BowTie")
team3=SoccerTeam("Cupcake")
team4=SoccerTeam("Posey")

team1.add_player(SoccerPlayer("60degres",TirLucarne()))

team2.add_player(SoccerPlayer("Classy",TirLucarne()))
team2.add_player(SoccerPlayer("Handsome",inter_strat))



team3.add_player(SoccerPlayer("Vanille",TirLucarne()))
team3.add_player(SoccerPlayer("Chocolat",Goal()))

team4.add_player(SoccerPlayer("Audmars-Piguet",Goal()))
team4.add_player(SoccerPlayer("Omega",FonceurStrategy()))
team4.add_player(SoccerPlayer("Cartier",TirLucarne()))
team4.add_player(SoccerPlayer("Rolex",TirLucarne()))


### Apprentissage

team_tree = SoccerTeam("Team Tree")

treeia=TreeIA(gen_feature_simple,dict(zip(list_nom,list_strat)))

fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"myfirsttree.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("Tree 2",TreeST))



teams =[team2,team3,team4,team1,team_tree]
teams1=[team2,team3,team4,team1,team_tree]

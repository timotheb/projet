# -*- coding: utf-8 -*-

from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
from soccersimulator import GAME_HEIGHT,GAME_WIDTH, GAME_GOAL_HEIGHT
import pickle


"""strategie de test"""
class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
	return SoccerAction(Vector2D.create_random(-0.1,0.1),Vector2D.create_random(-0.1,0.1))
    def copy(self):
        return RandomStrategy()



"""strategie de retard"""
class FonceurStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dis=(state.ball.position-player.position)
        if(teamid==1):
            pos = state.ball.position-player.position+state.ball.speed
            shoot = state.get_goal_center(2)-player.position
        else:
            pos = state.ball.position-player.position+state.ball.speed
            shoot = state.get_goal_center(1)-player.position
        if(PLAYER_RADIUS+BALL_RADIUS)<(dis.norm):
		shoot=Vector2D(0,0)
        return SoccerAction(pos,shoot)
    def copy(self):
        return FonceurStrategy()



"""aller vers la balle"""
class AllerVersB(SoccerStrategy):
    def __init__(self):
        self.name="AllerVersB"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D(0,0)
        pos = state.ball.position-player.position
        return SoccerAction(pos,shoot)
    def copy(self):
        return AllerVersB()



"""tir au but"""        
class TirBut(SoccerStrategy):
    def __init__(self):
        self.name="TirBut"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        pos=Vector2D(0,0)        
        if(teamid==1):
            shoot = state.get_goal_center(2)-player.position
            return SoccerAction(pos,shoot)
        else:
            shoot = state.get_goal_center(1)-player.position
            return SoccerAction(pos,shoot)
    def copy(self):
        return TirBut()


"""statique"""
class Static(SoccerStrategy):
    def __init__(self):
        self.name="Static"      
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(0,0),Vector2D(0,0))
    def copy(self):
        return Static()



"""goal"""
class Goal(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            dis=(state.ball.position-player.position)
            p=player.position
            if(state.ball.position.y<(GAME_HEIGHT*0.5)):
                shoot=Vector2D(10,10)
            else:
                shoot=Vector2D(10,-10)
            if (teamid==1):
                a=(state.ball.position+state.ball.speed+state.get_goal_center(1))
                a.x=a.x/2.0
            else:
                shoot.x=-10
                a=(state.ball.position+state.ball.speed+state.get_goal_center(2))
                a.x=a.x/2.1             
            a.y=a.y/2+0.35*(state.ball.position.y+state.ball.speed.y-45)
            a=a-p
            if((PLAYER_RADIUS+BALL_RADIUS)<(dis.norm)):
			shoot=Vector2D(0,0)
            return SoccerAction(a,shoot)  
    def copy(self):
        return Goal()

"""goalv2"""
class Goalv2(SoccerStrategy):
    def __init__(self):
        self.name="Goalv2"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            dis=(state.ball.position-player.position)
            p=player.position
            if(state.ball.position.y<(GAME_HEIGHT*0.5)):
                shoot=Vector2D(10,10)
            else:
                shoot=Vector2D(10,-10)
            if (teamid==1):
                a=(state.ball.position+state.ball.speed+state.get_goal_center(1))
                a.x=a.x/2.0
            else:
                shoot.x=-10
                a=(state.ball.position+state.ball.speed+state.get_goal_center(2))
                a.x=a.x/2.0             
            a.y=a.y/2+0.48*(state.ball.position.y+state.ball.speed.y-45)
            a=a-p
            if((PLAYER_RADIUS+BALL_RADIUS)>((dis+state.ball.speed).norm)):
                a=Vector2D(0,0)
            return SoccerAction(a,shoot)  
    def copy(self):
        return Goalv2()



class Aleatoire(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(need.get(teamid))
        b = state.ball.position
        dist= b - player.position
        gb = state.get_goal_center(need.get(teamid)) - player.position
        shoot = Vector2D.create_polar(gb.angle + random.uniform(-1,1),g.norm)
        return SoccerAction(dist,shoot)
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass          

class TirerRd(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.get(teamid))
        b = state.ball.position
        gb = state.get_goal_center(self.get(teamid)) - player.position
        de=Vector2D.create_polar(player.angle, g.norm)
        dr= Vector2D.create_polar(player.angle+random.random(),g.norm)
        direc = Vector2D()
        return SoccerAction(direc,dr)
    def create_strategy(self):
        return TirerRd()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1 


class TirLucarne(SoccerStrategy):
    def __init__(self):
        self.name="TirLucarne"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(2)
        dis=(state.ball.position-player.position)
        b = state.ball.position+state.ball.speed
        p=player.position
        bp = b-p
        bp.x=bp.x*1.2
        bp.y=bp.y*1.2
        if teamid==2:
            bp.x=bp.x+0.5
        else:
            bp.x=bp.x-0.5
        if(p.y>(GAME_HEIGHT/2)):
            shoot=Vector2D(GAME_WIDTH,GAME_HEIGHT/2+GAME_GOAL_HEIGHT/2-0.5)-state.ball.position-state.ball.speed
        else:
            shoot=Vector2D(GAME_WIDTH,GAME_HEIGHT/2-GAME_GOAL_HEIGHT/2+0.5)-state.ball.position-state.ball.speed
        if (teamid==2):
            if(p.y>(GAME_HEIGHT/2)):
                shoot=Vector2D(0,GAME_HEIGHT/2+GAME_GOAL_HEIGHT/2-0.5)-state.ball.position-state.ball.speed
            else:
                shoot=Vector2D(0,GAME_HEIGHT/2-GAME_GOAL_HEIGHT/2+0.5)-state.ball.position-state.ball.speed
        if((PLAYER_RADIUS+BALL_RADIUS)<(dis.norm)):
			shoot=Vector2D(0,0)
        return SoccerAction(bp,shoot)
    def create_strategy(self):
        return TirLucarne()

class DepHaut(SoccerStrategy):
    def __init__(self):
        self.name="Haut"    
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(0,2),Vector2D(0,0))
    def create_strategy(self):
        return DepHaut()   


class DepBas(SoccerStrategy):
    def __init__(self):
        self.name="Bas"    
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(0,-2),Vector2D(0,0))
    def create_strategy(self):
        return DepBas() 


class DepGauche(SoccerStrategy):
    def __init__(self):
        self.name="Gauche"    
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(-2,0),Vector2D(0,0))
    def create_strategy(self):
        return DepGauche() 
        
class DepDroite(SoccerStrategy):
    def __init__(self):
        self.name="Droite"    
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(2,0),Vector2D(0,0))
    def create_strategy(self):
        return DepDroite() 
    
    
    
    
    
    
"""selecteur de strats"""

"""class SelectorStrategy(ListStrategy):
    def __init__(self):
        self.name="Selecteur elegant"
        self.strategies = [TirLucarne,Goalv2]
        self.list_cond = [outil.posBX(state)]
    def selector(self,state,player,teamid):
        for i,cond in enumerate(self.list_cond):
            if cond:
                return i
        return -1
    def compute_strategy(self,state,player,teamid):
        return self.strategies[self.selector(state,player,teamid)].compute_strategies(state,player,teamid)"""

"""class Attaquant(SoccerStrategy):
	def __init__(self):
		self.bal= ComposeStrategy(AllerVersBalle(),TirerRd())
		self.fonce = FonceurStrategy()
		self.ale = ComposeStrategy(AllerVersBalle(),Aleatoire())
	def compute_strategy(self,state,player,teamid):
		g = state.get_goal_center(self.getad(teamid))
		gadv = state.get_goal_center(need.get(teamid))
		b = state.ball.position
		gadvb = gadv - b
		dist= b - player.position
		gb = g - b
		if ((b.x==GAME_WIDTH/2.0 and b.y==GAME_HEIGHT/2.0) or (gadvb.norm < GAME_WIDTH/6.0)):
			return self.bal.compute_strategy(state,player,teamid)
		elif gb.norm < GAME_WIDTH/8.0:
			return self.ale.compute_strategy(state,player,teamid)
		else:
			return self.fonce.compute_strategy(state,player,teamid)
	def start_battle(self,state):
		pass
	def finish_battle(self,won):
		pass
	def getad(self,teamid):
		if(teamid == 1):
			return 1
		else:
			return 2       
""" 

"""diriger vers un point"""
"""class DirPoint(SoccerStrategy):
    def __init__(self,Vector2D()):
        self.point=Vector2D(x,y)        
        self.name="VersPoint"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot=Vector()
        dist = self.point - player.position
        return SoccerAction(dist,shoot)          
    def copy(self):
        return DirPoint()
    def create_strategy(self):
        return DirPoint() """
        
        
"""se met en position de goal puis fonce sur la balle"""        
"""class GoalToGoal(SoccerStrategy):
    def __init__(self):
        self.name="GtoG"
        stop=0
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        if(stop==0):      
            if(PLAYER_RADIUS+BALL_RADIUS>state.ball.position-player.position):
                TirBut.compute_strategy
                stop=1
            else:
                return SoccerAction(Vector2D(0,0),Vector2D(0,0))
        else:
            FonceurStrategy.comput_startegy
    def copy(self):
        return GoalToGoal()
    def create_strategy(self):
        return GoalToGoal()    """

"""passe simple"""       
"""class PasseSimple(SoccerStrategy):
    def __init__(self):
        self.name="PasseS"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        
        
        pos = state.ball.position-player.position
        shoot = Vector2D.create_random(-5,5)
        return SoccerAction(pos,shoot)
    def copy(self):
        return PasseSimple()
    def create_strategy(self):
        return PasseSimple()"""


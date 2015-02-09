from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS


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
    def create_strategy(self):
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
    def create_strategy(self):
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
    def create_strategy(self):
        return TirBut()        
        
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
    def create_strategy(self):
        return Static()

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
"""goal"""
class Goal(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        if(teamid==1):            
            a= (ball.position-state.get_goal_center(2))/2
            




            

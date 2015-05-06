from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
from soccersimulator import GAME_HEIGHT,GAME_WIDTH, GAME_GOAL_HEIGHT

"""rend True si le ballon est sur la partie basse du terrain et faux sinon"""
class outil(SoccerStrategy):
    def posBY(state):
        if(state.ball.position.y<(GAME_HEIGHT/2)):
            return True
        else:
            return False



      
    def posBX(state):
        if(teamid==1):
            if(state.ball.position.x<(GAME_WIDTH/2)):
                return True
            else:
                return False 
        else: 
            if(state.ball.position.x<(GAME_WIDTH/2)):
                return False
            else:
                return True 
    
    def canShoot(state):
        if((PLAYER_RADIUS+BALL_RADIUS)<(state.ball.position-player.position).norm):
            return True
        else:
            return False

    def miroir(object):
        object.x=-object.x
        return object

    def allerVers(object,state):
        return object-player.posistion
    
    def ballInMud(state):
        for zone in state.danger_zones:
            if (zone.contains(state.ball.position) and zone.type=="mud"):
                return True 
        return False
    
    def ballInIce(state):
        for zone in state.danger_zones:
            if (zone.contains(state.ball.position) and zone.type=="ice"):
                return True 
        return False
        
    def playerInMud(state):
        for zone in state.danger_zones:
            if (zone.contains(player.position) and zone.type=="mud"):
                return True 
        return False
    
    def playerInIce(state):
        for zone in state.danger_zones:
            if (zone.contains(player.position) and zone.type=="ice"):
                return True 
        return False    
    
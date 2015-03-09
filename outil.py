from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
from soccersimulator import GAME_HEIGHT,GAME_WIDTH, GAME_GOAL_HEIGHT

"""rend True si le ballon est sur la partie basse du terrain et faux sinon"""
class tool(SoccerStrategy):
    def posBX(state):
        if(state.ball.position<(GAME_HEIGHT/2)):
            return True
        else:
            return False
    
    
    
    def miroir(object):
        object.x=-object.x
        return object
    def allerVers(Vector2D,)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:38:17 2015

@author: 3301393
"""

from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import os

from soccersimulator import *
import strats

# Quelques generateurs de features
def teamid(state,teamid,playerid):
    return teamid
    
def posXB(state,teamid,playerid):
    return state.ball.position.x
    
def posYB(state,teamid,playerid):
    return state.ball.position.y

def spXB(state,teamid,playerid):
    return state.ball.speed.x
    
def spYB(state,teamid,playerid):
    return state.ball.speed.y
    
    
def distance_ball(state,teamid,playerid):
    return (state.get_team(teamid)[playerid].position-state.ball.position).norm

def distance_mon_but(state,teamid,playerid):
    return (state.get_goal_center(teamid)-state.get_team(teamid)[playerid].position).norm

def distance_autre_but(state,teamid,playerid):
    return (state.get_goal_center(3-teamid)-state.get_team(teamid)[playerid].position).norm

def distance_ball_mon_but(state,teamid,playerid):
    return (state.get_goal_center(teamid)-state.ball.position).norm


def distance_ball_autre_but(state,teamid,playerid):
    return (state.get_goal_center(3-teamid)-state.ball.position).norm



list_fun_features=[teamid,posXB,posYB,spXB,spYB,distance_ball,distance_mon_but,distance_autre_but,distance_ball_mon_but,distance_ball_autre_but]

# Une fonction de generation de feature.
# np.array permet de transformer en vecteur une liste
def gen_feature_simple(state,teamid,playerid):
    return np.array([f(state,teamid,state.get_player(teamid,playerid)) for f in list_fun_features])

def app():
    treeia=TreeIA(gen_feature_simple)
    treeia.learn(fn="tent3.4.pkl")
    treeia.save("tree3.pkl")
    treeia.to_dot("tree3.dot")
    """ dot -Tpdf myfirstree.dot -o tree.pdf"""
    
    
#app()
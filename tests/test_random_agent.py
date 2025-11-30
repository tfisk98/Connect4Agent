"""
Testing the class RandomAgent from random_agent.py.
WARNING : Working directory must be the parent of this file's directory
"""


### Working directory must be the parent of this file's directory

import sys
import os
sys.path.append(os.getcwd())

import src.random_agent as rnda
import src.game_facilities as gf


### Testing RandomAgent against himself, checking ML-Arena requirements and statistical
### expected winrate range with a mild advantage for the agent that play first


def test_RandomAgent() :
    stats=gf.connect4_game_with_stats(1000, rnda.RandomAgent, rnda.RandomAgent)
    minimal_win_rate0 = 0.5
    minimal_win_rate1 = 0.4
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1 = stats[1]["Maximum memory usage peak"]["player_1"]
    assert stat_win_rate0 > minimal_win_rate0
    assert stat_win_rate1 > minimal_win_rate1 and stat_win_rate1 < minimal_win_rate0
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    assert stat_maximum_peak1 < maximum_memory_peak
    return


### Testing WeightedRandomAgent against RandomAget, WeeightedRandom Agent plays first : checking 
### ML-Arena requirements and statistical superiority of WeightedRandomAgent

def test_WeightedRandomAgent_first() :
    stats=gf.connect4_game_with_stats(1000, rnda.WeightedRandomAgent, rnda.RandomAgent)
    minimal_win_rate = 0.8
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate0 = stats[1]["Frequency of win"]["player_0"]
    stat_maximum_time0 = stats[1]["Maximum time to play"]["player_0"]
    stat_maximum_peak0 = stats[1]["Maximum memory usage peak"]["player_0"]
    assert stat_win_rate0 > minimal_win_rate
    assert stat_maximum_time0 < maximum_time
    assert stat_maximum_peak0 < maximum_memory_peak
    return


### Testing WeightedRandomAgent against RandomAget, WeeightedRandom Agent plays second : checking 
### ML-Arena requirements and statistical superiority of WeightedRandomAgent


def test_WeightedRandomAgent_second() :
    stats=gf.connect4_game_with_stats(1000, rnda.RandomAgent, rnda.WeightedRandomAgent)
    minimal_win_rate = 0.75
    maximum_time = 2.8
    maximum_memory_peak = 364*10e6
    stat_win_rate1 = stats[1]["Frequency of win"]["player_1"]
    stat_maximum_time1 = stats[1]["Maximum time to play"]["player_1"]
    stat_maximum_peak1 = stats[1]["Maximum memory usage peak"]["player_1"]
    assert stat_win_rate1 > minimal_win_rate
    assert stat_maximum_time1 < maximum_time
    assert stat_maximum_peak1 < maximum_memory_peak
    return
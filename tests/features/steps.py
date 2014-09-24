# -*- coding: utf-8 -*-
import app.match as m
from lettuce import *

@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_player1_and_player2_start_a_match_to_pacted_sets(step, player1, player2, pacted_sets):
    world.match = m.Match(player1, player2, int(pacted_sets))
    world.p1 = player1
    world.p2 = player2
    world.sets = int(pacted_sets)
    world.current_set = 0
    world.p1_scores = [0]
    world.p2_scores = [0]

@step(u'When: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def when_player1_and_player2_start_a_match_to_pacted_sets(step, player1, player2, pacted_sets):
    assert "{0} plays with {1} | 0-0".format(player1, player2) == world.match.display_score(), \
        world.match.display_score()


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score(step, expected_score):
    assert expected_score == world.match.display_score(), \
        world.match.display_score()

@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_player_won_the_1st_set(step, player, game_set, p1_score, p2_score):
    if world.current_set == 0:
        if world.p1 == player:
            world.p1_scores[world.current_set] = int(p1_score)
            world.p2_scores[world.current_set] = int(p2_score)
            world.match.set_scores(int(p1_score), int(p2_score))
        elif world.p2 == player:
            world.p1_scores[world.current_set] = int(p2_score)
            world.p2_scores[world.current_set] = int(p1_score)
            world.match.set_scores(int(p2_score), int(p1_score))


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_player_won_the_set(step, player, game_set, p1_score, p2_score):
    if int(game_set[0]) <= world.sets:
        #if (world.current_set + 1) <= int(game_set[0]):
        world.current_set += 1
        world.p1_scores.append(0)
        world.p2_scores.append(0)
            
        if world.p1 == player:
            world.p1_scores[world.current_set] = int(p1_score)
            world.p2_scores[world.current_set] = int(p2_score)
            world.match.set_scores(int(p1_score), int(p2_score))
        elif world.p2 == player:
            world.p1_scores[world.current_set] = int(p2_score)
            world.p2_scores[world.current_set] = int(p1_score)
            world.match.set_scores(int(p2_score), int(p1_score))


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is(step, expected_score):
    assert expected_score == world.match.display_score(), \
        world.match.display_score()


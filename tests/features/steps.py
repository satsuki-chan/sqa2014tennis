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
#def then_i_see_score_group1(step, group1):
def then_i_see_score(step, expected_score):
    #scores = " ".join(", {0}-{1}".format(scores1, scores2) for scores1 in world.p1_scores for scores2 in world.p2_scores)
    #
    #if world.current_set == 0 and world.p1_scores[world.current_set] < 3 and world.p2_scores[world.current_set] < 3:
    #    score_to_assert = "{0} plays with {1} | {2}".format(world.p1, world.p2, scores[2:])
    #elif sum(world.p2_scores) > sum(world.p1_scores):
    #    scores = " ".join(", {1}-{0}".format(scores1, scores2) for scores1 in world.p1_scores for scores2 in world.p2_scores)
    #    score_to_assert = "{1} defeated {0} | {2}".format(world.p1, world.p2, scores[2:])
    #else:
    #    score_to_assert = "{0} defeated {1} | {2}".format(world.p1, world.p2, scores[2:])
    
    #assert "{0} plays with {1} | {2}".format(world.p1, world.p2, scores[2:]) == world.match.display_score(), \
    #assert score_to_assert == world.match.display_score(), \
    assert expected_score == world.match.display_score(), \
        world.match.display_score()

@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
#def when_group1_won_the_group2_set_group3_group4(step, group1, group2, group3, group4):
def when_player_won_the_1st_set(step, player, game_set, p1_score, p2_score):
    #assert False, 'This step must be implemented'
    if world.current_set == 0:
        if world.p1 == player:
            world.p1_scores[world.current_set] = int(p1_score)
            world.p2_scores[world.current_set] = int(p2_score)
            world.match.set_scores(int(p1_score), int(p2_score))
        elif world.p2 == player:
            world.p1_scores[world.current_set] = int(p2_score)
            world.p2_scores[world.current_set] = int(p1_score)
            world.match.set_scores(int(p2_score), int(p1_score))
        
        #world.current_set += 1
        #world.p1_scores.append(0)
        #world.p2_scores.append(0)        
    #print("player1 = " + player1 + ", player2 = " + player2)
    #assert "{0} defeated with {1} | {2}-{3}".format(world.p1, world.p2, p1_score, p2_score) == world.match.display_score(), \
    #    world.match.display_score()

@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
#def and_group1_won_the_group2_set_group3_group4(step, group1, group2, group3, group4):
#def and_player_won_the_2nd_set(step, player1, player2, p1_score, p2_score):
def and_player_won_the_set(step, player, game_set, p1_score, p2_score):
    #assert False, 'This step must be implemented'
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
    
    #print("player1 = " + player1 + ", player2 = " + player2)
    #assert "{0} defeated with {1} | {2}-{3}, {4}-{5}".format(world.p1, world.p2, world.set1_p1_score, world.set1_p2_score, p1_score, p2_score) == world.match.display_score(), \
    #    world.match.display_score()


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is(step, expected_score):
    #scores = " ".join(", {0}-{1}".format(scores1, scores2) for scores1 in world.p1_scores for scores2 in world.p2_scores)
    #
    #if world.current_set == 0 and world.p1_scores[world.current_set] < 3 and world.p2_scores[world.current_set] < 3:
    #    score_to_assert = "{0} plays with {1} | {2}".format(world.p1, world.p2, scores[2:])
    #elif sum(world.p2_scores) > sum(world.p1_scores):
    #    scores = " ".join(", {1}-{0}".format(scores1, scores2) for scores1 in world.p1_scores for scores2 in world.p2_scores)
    #    score_to_assert = "{1} defeated with {0} | {2}".format(world.p1, world.p2, scores[2:])
    #else:
    #    score_to_assert = "{0} defeated with {1} | {2}".format(world.p1, world.p2, scores[2:])

    #assert "{0} defeated with {1} | {2}-{3}, {4}-{5}".format(world.p1, world.p2, world.set1_p1_score, world.set1_p2_score, world.set2_p1_score, world.set2_p2_score) == world.match.display_score(), \
    #assert score_to_assert == world.match.display_score(), \
    assert expected_score == world.match.display_score(), \
        world.match.display_score()



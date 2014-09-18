# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_player1_and_player2_start_a_match_to_pacted_sets(step, player1, player2, pacted_sets):
    world.match = m.Match(player1, player2, pacted_sets)
    world.p1 = player1
    world.p2 = player2
    world.sets = pacted_sets

@step(u'When: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def when_player1_and_player2_start_a_match_to_pacted_sets(step, player1, player2, pacted_sets):
    #assert False, 'This step must be implemented'
    assert "{0} plays with {1} | 0-0".format(player1, player2) == world.match.display_score(), \
        world.match.display_score()


@step(u'Then: I see score: "([^"]*)"')
#def then_i_see_score_group1(step, group1):
def then_i_see_score(step, player1):
    #assert False, 'This step must be implemented'
    assert "{0} plays with {1} | 0-0".format(world.p1, world.p2) == world.match.display_score(), \
        world.match.display_score()

@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, group1, group2, group3, group4):
    assert False, 'This step must be implemented'


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, group1, group2, group3, group4):
    assert False, 'This step must be implemented'


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, group1):
    assert False, 'This step must be implemented'



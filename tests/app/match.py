# -*- coding: utf-8 -*-
class Match:
    def __init__(self,player1,player2,pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets

    def display_score(self):
        return "{0} plays with {1} | 0-0".format(self.p1, self.p2)

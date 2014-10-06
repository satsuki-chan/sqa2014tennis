# -*- coding: utf-8 -*-
class Match:
    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.current_set = 0
        self.p1_scores = [int(0)]
        self.p2_scores = [int(0)]

    def display_score(self):
        scores = ""
        index = 0
        while index <= self.current_set:
            scores += "".join(", {0}-{1}".format(self.p1_scores[index], self.p2_scores[index]))
            index += 1

        total_score1 = 0
        total_score1 = sum(self.p1_scores)
        total_score2 = 0
        total_score2 = sum(self.p2_scores)

        if self.current_set == 0 and self.p1_scores[self.current_set] < 3 and self.p2_scores[self.current_set] < 3:
            current_score = "{0} plays with {1} | {2}".format(self.p1, self.p2, scores[2:])
        elif total_score2 >= total_score1:
            scores = ""
            index = 0
            while index <= self.current_set:
                scores += "".join(", {1}-{0}".format(self.p1_scores[index], self.p2_scores[index]))
                index += 1

            current_score = "{1} defeated {0} | {2}".format(self.p1, self.p2, scores[2:])
        else:
            current_score = "{0} defeated {1} | {2}".format(self.p1, self.p2, scores[2:])

        return current_score

#    def player_scores(self, scoring_player):
#        if (self.current_set + 1) <= self.pacted_sets:
#            test_winner = abs(self.p1_scores[self.current_set] - self.p2_scores[self.current_set])
#            if (self.p1_scores[self.current_set] >= 4 or self.p2_scores[self.current_set] >= 4) and test_winner >= 2:
#                self.current_set += 1
#                self.p1_scores.append(0)
#                self.p2_scores.append(0)
#
#            if 1 == scoring_player:
#                self.p1_scores[self.current_set] += 1
#            elif 2 == scoring_player:
#                self.p2_scores[self.current_set] += 1
#
#        return self

    def set_scores(self, score_p1, score_p2):
        if (self.current_set + 1) <= self.pacted_sets:
            test_winner = abs(self.p1_scores[self.current_set] - self.p2_scores[self.current_set])
            if (self.p1_scores[self.current_set] >= 4 or self.p2_scores[self.current_set] >= 4) and test_winner >= 2:
                self.current_set += 1
                self.p1_scores.append(0)
                self.p2_scores.append(0)

            self.p1_scores[self.current_set] = score_p1
            self.p2_scores[self.current_set] = score_p2

        return self

# This Python file uses the following encoding: utf-8


class IA:
    def __init__(self):
        pass

    #Je n'ai que défini mon minimax, il n'est pas implémenter quelque part dans le code.
    def miniMax(self, node, depth, maximizingPlayer, nbrPionsTeamN, nbrPionsTeamB):
        if depth == 0 or nbrPionsTeamN == 0 or nbrPionsTeamB == 0:
            return
        if maximizingPlayer == True:
            cost = -1000
            for child in node:
                cost = max(cost, self.miniMax(child, depth - 1, False))
                return cost
        else:
            cost = 1000
            for child in node:
                cost = max(cost, self.miniMax(child, depth - 1, True))
                return cost


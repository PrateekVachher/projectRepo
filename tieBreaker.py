import random

class TieBreaker:
    def flipCoin(self):
        res = random.randint(0,1)
        return res

    def tieBreak(self, candidates):
        count0 = 0
        count1 = 0
        for x in range(1001):
            if self.flipCoin() == 0:
                count0 += 1
            else:
                count1 += 1
        if count0 > count1:
            return candidates[0]
        else:
            return candidates[1]


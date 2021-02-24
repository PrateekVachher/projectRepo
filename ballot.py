class Ballot:
    def __init__(self, bNum, choices):
        self.bNum = bNum
        self.choices = choices # len of choices is number of candidates

    def getChoice(self, choiceNum, candidates):
        candidateIndex = self.choices.index(choiceNum)
        if candidateIndex == -1:
            return None
        else:
            return candidates[candidateIndex]
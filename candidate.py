class Candidate:
    def __init__(self, cName, cParty):
        self.cName = ""
        self.cParty = ""
        self.votes = [] # list of Ballot Numbers assigned
    
    def getVote(self, bNum):
        self.votes.append(bNum)
    
    def getVoteCount(self):
        return len(self.votes)
    
    def getBallotList(self):
        return self.votes
from fileHandling import FileHandling
from candidate import Candidate
from ballot import Ballot
import math

class IR:
    def __init__(self, fileName):
        self.fileName = fileName
        self.fileHandler = FileHandling(fileName)
        self.ballots = {}  # Hash Map with instances of Ballots
        self.candidates = {}  # Hash map of Candidate Instances
        self.candidateNames = []
        self.numOfBallots = 0
        self.neededForMajority = 0
    
    def getCandidates(self):
        candidates = self.fileHandler.readLine()
        candidateNames = candidates.split(",")
        for candidateName in candidateNames:
            candidateName = candidateName.strip()
            cName = candidateName[:-3]
            cParty = candidateName[-2]
            candidateInstance = Candidate(cName, cParty)
            self.candidates[cName] = candidateInstance
            self.candidateNames.append(cName)
    
    def readBallots(self):
        for ballotCounter in range(self.numOfBallots):
            ballotChoices = self.fileHandler.readLine().strip().split(",")
            for x in range(len(ballotChoices)):
                if ballotChoices[x] == "":
                    ballotChoices[x] = None
                else:
                    ballotChoices[x] = int(ballotChoices[x])

            ballotInstance = Ballot(ballotCounter, ballotChoices)
            self.ballots[ballotCounter] = ballotInstance
            ballotWinner = ballotInstance.getChoice(1, self.candidateNames)
            self.candidates[ballotWinner].getVote(ballotInstance.bNum)
            print ("Ballot #",ballotCounter, "is assigned to", ballotWinner)

    def loadBallots(self):
        self.getCandidates()
        self.numOfBallots = int(self.fileHandler.readLine())
        self.neededForMajority = math.ceil(self.numOfBallots / 2)
        self.readBallots()


    def process(self):
        self.loadBallots()
        noWinner = True
        voteCount = {}
        while (noWinner):
            for x in self.candidates:
                print (x, self.candidates[x].getVoteCount())
                voteCount[x] = self.candidates[x].getVoteCount()
            print ("highest count", max(list(voteCount.values())))
        
from audit import Audit 
from ballot import Ballot
from candidate import Candidate
from fileHandling import FileHandling
from IR import IR
from media import Media
from OPL import OPL
from party import Party
from tieBreaker import TieBreaker

import os

class Main:
    def run(self):
        fileName = input("Enter Filename: ")
        if fileName in os.listdir("./"):
            loop = True
            while loop:
                print("Enter")
                print("\t 1 for Instant Run Off")
                print("\t 2 for Open Party Listing")
                print("\t 0 to Exit")
                typeOfElection = input()
                if typeOfElection == "1":
                    loop = False
                    election = IR(fileName)
                    election.process()
                elif typeOfElection == "2":
                    loop = False
                    pass # OPL            
                elif typeOfElection == "0":
                    loop = False
                else:
                    print ("Incorrect Entry")

        else:
            print ("File Not Found")

a = Main()
a.run()
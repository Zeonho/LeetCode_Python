"""

In a town, there are N people labelled from 1 to N.  There is a rumor that one 
of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the 
person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town 
judge.  Otherwise, return -1.

"""


"""
Thoughts:
1. Find EveryBody

Note:
dict:
if i in dict
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # N = 1
        # len(trust) = 0
        if len(trust) == 0 and N == 1:
            return 1
        
        people_trust_others = self.findEveryBody(trust)

        is_trust = self.trustDict(trust)
        
        
        for p, t in is_trust.items():
            if p not in people_trust_others and t == N - 1:
                return p

        return -1

    def findEveryBody(self, trust):
        people = []
        for person in trust:
            people.append(person[0])
        return set(people)
    
    def trustDict(self, trust):
        dic = dict()
        for person in trust:
            if person[1] in dic:
                dic[person[1]] += 1
            else:
                dic[person[1]] = 1
        return dic


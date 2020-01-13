"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

class Solution:
    def letterCasePermutationRec(self, lst, S):
            #Base Case
            if len(S) == 0:
                return lst
            #Induction Steps
            else:
                if S[0].isalpha():
                    # 1. Empty Inside -> add two new one
                    # 2. Have Some S:b -> ["a1", "A1"] -> 1.add to existed, 2. add two more
                    if len(lst) == 0:
                        lst.append(S[0].lower())
                        lst.append(S[0].upper())
                        return self.letterCasePermutationRec(lst, S[1:])
                    else:
                        new_lst = []
                        for each_str in lst:
                            new_lst.append(each_str + S[0].lower())
                            new_lst.append(each_str + S[0].upper())
                        return self.letterCasePermutationRec(new_lst, S[1:])
                # Digits or anything else
                else:
                    new_lst = []
                    if len(lst) == 0:
                        new_lst.append(S[0])
                    else:
                        for each_str in lst:
                                new_lst.append(each_str + S[0])
                    return self.letterCasePermutationRec(new_lst, S[1:])
                    

    def letterCasePermutation(self, S: str) -> List[str]:
        # Every Letter has 2 possible
        # Total is 2^n possibilities, n is number of letter
        
        # Brain Storming
        # 1. If follow the sequence, a1b2 -> A1b2 -> a1b2 -> a1B2 X
        # 2. Stack? Queue? Scan once added both [a,A,b,B] X
        # 3. Recursion
        
        lst = []
        
        return self.letterCasePermutationRec(lst, S)
        
        
    
            
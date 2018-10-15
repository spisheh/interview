"""

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


**********************
12 / 12 test cases passed.
Runtime: 64 ms
Runtime beats 90.41 % of python3 submissions.

"""

class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words={}
        for i,w in enumerate(words):
            if w in self.words:
                self.words[w].append(i)
            else:
                self.words[w]=[i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1=self.words[word1]
        list2=self.words[word2]
        if not list1 or not list2:
            return -1
        diff=abs(list1[0]-list2[0])
        i=0
        j=0
        while i<len(list1) and j<len(list2):
            diff=min(diff, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i+=1
            else:
                j+=1
                
        return diff
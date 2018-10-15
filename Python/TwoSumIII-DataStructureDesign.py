"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


****************************
16 / 16 test cases passed.
Runtime: 88 ms
Runtime beats 97.92 % of python3 submissions.

"""

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set=set()
        self.double=set()
        self.cache=set()
        self.min=float('Inf')
        self.max=-float('Inf')
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.set:
            self.set.add(number)
        else:
            self.double.add(number)
        double = 2*number
        self.min=min(self.min, double)
        self.max=max(self.max, double)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in self.cache:
            return True
        if value < self.min or self.max < value:
            return False
        for num in self.set:
            comp = value-num
            if comp in self.set and (comp!=num or comp in self.double):
                if len(self.cache) < 1024:
                    self.cache.add(value)
                return True
        return False

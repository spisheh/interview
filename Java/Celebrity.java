/*
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is
to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity
(or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function
int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. 
Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

*************Note***********
171 / 171 test cases passed.
Runtime: 8 ms
Runtime beats 99.84% of java submitions.
*/
public class Solution extends Relation {
    /** Finds next possible celebrity */ 
    private int pos(int i, int n){
        int cel=i++;
        while( i < n ){
            if (knows(cel,i)){
                cel = i;
            }
           i++;
        }
        return cel;
    }
  
    /** Checks if input has all the celebrity requirement*/ 
    private boolean check(int cel, int n){
        for (int j=0; j < cel; j++){
            if (knows(cel,j) || !knows(j,cel)){
                return false;
            }
        }
        for (int i=cel+1; i < n; i++){
            if (!knows(i,cel)){
                return false;
            }
        }
        return true;
    }
  
    /** search for the celebrity */
    public int findCelebrity(int n) {
        int cel=0;
        while (cel < n){
            cel=pos(cel,n);
            if (check(cel,n)){
                return cel;
            }
            cel++;
        }
        return -1;
    }
}

public class Solution extends Relation {
    /** Finds next possible celebrity */ 
    private int pos(int i, int n){
        int cel=i;
        i++;
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

/*
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

*****************Note*****************
601 / 601 test cases passed.
Runtime: 3 ms
Runtime beats 92.86 of java submitions.

*/


class Solution {

    /** convert numbers under 1000 to English words*/
    private ArrayList UnderHundred(int num){
        ArrayList<String> out = new ArrayList<String>();
        int intOne = num % 10;
        int intTen = (num % 100)/10;
        int inthundred = (num)/100;
        
        if (inthundred!=0 ){
            out.add(ones(inthundred)+" Hundred");
        }
        if (intTen == 1){
            out.add(teens(num % 100));
        }
        else if (intTen != 0){
            out.add(tens(intTen));
        }
        if (intOne!=0 && intTen!=1){
            out.add(ones(intOne));
        }

        return out;
    }
    
    
    
    
    /** convert numbers under 10 to English words */
    private String ones(int num){
        String out="";
        switch (num){
            case 1: return "One";
            case 2: return "Two";
            case 3: return"Three";
            case 4: return"Four";
            case 5: return"Five";
            case 6: return"Six";
            case 7: return"Seven";
            case 8: return"Eight";
            case 9: return"Nine"; 
        }
        return "\b";
    }
    
    
    
    
    /** convert tens' place of numbers to English words */
    private String tens(int num){
        String out="";
        switch (num){
            case 2: return "Twenty";
            case 3: return"Thirty";
            case 4: return"Forty";
            case 5: return"Fifty";
            case 6: return"Sixty";
            case 7: return"Seventy";
            case 8: return"Eighty";
            case 9: return"Ninety"; 
        }
        return "\\b";
    }
    
    
    
    
    /** convert numbers between 10 and 20 to English words */
    private String teens(int num){
        String out="";
        switch (num){
            case 10: return "Ten";
            case 11: return "Eleven";
            case 12: return "Twelve";
            case 13: return"Thirteen";
            case 14: return"Fourteen";
            case 15: return"Fifteen";
            case 16: return"Sixteen";
            case 17: return"Seventeen";
            case 18: return"Eighteen";
            case 19: return"Nineteen"; 
        }
        return "";
    }
    
    
    
    
    /** Main Function which convert integers to English words */
    public String numberToWords(int num) {
        if (num==0){
            return "Zero";
        }
        int i=0;
        ArrayList<String> res = new ArrayList<String>();
        int temp = 0;
        
        while (num > 0){
            temp = num % 1000;
            if (temp>0){
                switch (i){
                case 1: res.add(0,"Thousand");
                    break;
                case 2: res.add(0,"Million");
                    break;
                case 3: res.add(0,"Billion");
                    break;  
                }
                res.addAll(0,UnderHundred(temp));    
            }
            num= (int) num / 1000;
            i++;
        }
        
        String out= (String) res.get(0);
        for(int j=1; j < res.size(); j++){
            out += " "+res.get(j);
        }
        return out;
    }
    
}

class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int max=0;
        for(int i=0;i<s.length();i++){
            String seen="";
            for(int j=i;j<s.length();j++){
                if(seen.contains(String.valueOf(s.charAt(j)))){
                    break;
                }         
                else{
                    seen+=s.charAt(j);
                }
                   }

            max=Math.max(max,seen.length());

        }
        return max;

    }
}
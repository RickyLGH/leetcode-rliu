class Solution {
    public boolean isSubsequence(String s, String t) {
        int strack = 0;
        String result = "";
        for(int i = 0; i < t.length(); i++){
            if(strack >= s.length()){
                return true;
            }
            if(t.charAt(i) == s.charAt(strack)){
                strack = strack + 1;
                result = result + t.charAt(i);
            }
        }
        System.out.print(result);
        return s.equals(result);
    }
}
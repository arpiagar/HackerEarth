class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
         List<Integer> intList = new ArrayList<Integer>();
         if (words.length == 0){ return intList;}
         
         Map<Character,Integer> wordsMap = calculateWordMap(words);
         int counter = words[0].length() * words.length;
         HashMap<String,Integer> wordMap = new HashMap<String,Integer>();
         for (String word: words ){
            if (wordMap.get(word) == null){
                    wordMap.put(word,1);
            }else{
                    wordMap.put(word, wordMap.get(word)+1);
            }
        }
         for (int i =0 ; i <= s.length()-counter ; i++) {
             Map<Character,Integer> freqMap = calculateCounterMap(s,i,i+counter-1);
            // System.out.println(freqMap);
             
             if (compareMaps(wordsMap, freqMap)){   
                 HashMap subMap = (HashMap) wordMap.clone();
                 String mainString = s.substring(i,i+counter);
                 int offset = words[0].length();
                 for(int j=0; j < words.length; j++){
                  String subString =  mainString.substring(offset*j, offset*(j+1));
                  if (subMap.get(subString) == null){
                      break;
                  } else{
                      if ((int)subMap.get(subString) == 1){
                          subMap.remove(subString);
                      }else{
                          subMap.put(subString,(int)subMap.get(subString)-1);
                      }
                  }
                 }
                 if (subMap.keySet().size()==0){
                     intList.add(i);
                 }
           //  System.out.println(wordsMap);
         }}
        return intList;
    }

    public Map<Character,Integer> calculateCounterMap(String s, int startIdx, int endIdx){
        HashMap<Character,Integer> freqMap = new HashMap<Character,Integer>();
        for(int i=startIdx; i <= endIdx ; i++) {
            if (freqMap.get(s.charAt(i)) !=null && freqMap.get(s.charAt(i))> 0){
                freqMap.put(s.charAt(i),freqMap.get(s.charAt(i))+1);
            }else{
                freqMap.put(s.charAt(i),1);
            }
        }
        return freqMap;
    }
    public Map<Character,Integer> calculateWordMap( String[] words){
        HashMap<Character,Integer> wordsMap = new HashMap<Character,Integer>();
        
        for (int i = 0; i < words.length; i++){
            for (int j = 0; j < words[0].length(); j++ ){
                 
                if(wordsMap.get(words[i].charAt(j)) !=null && wordsMap.get(words[i].charAt(j)) > 0 ){
                    wordsMap.put(words[i].charAt(j), 1+wordsMap.get(words[i].charAt(j) ));
                }else{
                    wordsMap.put(words[i].charAt(j), 1 );
                }
            }
        }
         return wordsMap; 
    }
    public boolean compareMaps(Map<Character,Integer> map1, Map<Character,Integer> map2){
        for (Character key : map1.keySet()){
            if (map2.get(key) == null){
                return false;
            }else{
                if (map1.get(key) != map2.get(key)){
                    return false;
                } else {
                    map2.remove(key);
                }
            }
        }
        if (map2.keySet().size() > 0) {
            return false;
        }
        return true;
    }
}

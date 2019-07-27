class MagicDictionary {

    /** Initialize your data structure here. */
    public MagicDictionary() {
        this.trie = new Trie();
    }

    /** Build a dictionary through a list of words */
    public void buildDict(String[] dict) {
        for (int i =0; i < dict.length; i++){
            String word = doct[i];
            addWordtoTrie(word);
        }
        return;
    }

    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    public boolean search(String word) {

    }
}
class Trie {
    Node root;
    public void Trie(){
        this.root  = new Node();
    }
    public Node addWordToTrie(Node root, String word){
            if word.length() == 1
            if (root.NodeMap.get(word[i]) ){
                addWordToTrie(root.NodeMap.get(word[i]), word.substring(1,word.length()))
            } else{
                root.NodeMap.put(word[i], new Node());
            }

    }
}
class Node {
    String nodeKey;
    Map<String,Object> nodeMap;

    public Node(String c){
       this.nodeKey = c;
        this.nodeMap();

   }
}
/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * boolean param_2 = obj.search(word);
 */

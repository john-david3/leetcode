class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_map = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.",
        "h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---",
        "p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--",
        "x":"-..-","y":"-.--","z":"--.."}

        output = set()
        for word in words:
            morse_str = ""
            for letter in word:
                morse_str += morse_map[letter]
            output.add(morse_str)

        return len(output)
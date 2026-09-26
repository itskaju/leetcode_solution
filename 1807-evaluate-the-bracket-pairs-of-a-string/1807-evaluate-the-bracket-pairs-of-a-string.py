class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # 1. Convert the knowledge list into a hash map for O(1) lookups
        dict_knowledge = {key: value for key, value in knowledge}
        
        ans = []
        is_key = False
        current_key = []
        
        # 2. Iterate through the string character by character
        for char in s:
            if char == '(':
                is_key = True
            elif char == ')':
                is_key = False
                key_str = "".join(current_key)
                # Append the value if the key exists, otherwise append '?'
                ans.append(dict_knowledge.get(key_str, '?'))
                current_key.clear()
            else:
                if is_key:
                    current_key.append(char)
                else:
                    ans.append(char)
                    
        return "".join(ans)

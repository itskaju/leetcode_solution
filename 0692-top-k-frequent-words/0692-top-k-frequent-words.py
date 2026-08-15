class Solution:
    def topKFrequent(self, words, k):
        freq = {}

        for word in words:
            freq[word] = freq.get(word,0) + 1

        sorted_words = sorted(freq, key= lambda word: (-freq[word], word))  

        return sorted_words[:k]  


    
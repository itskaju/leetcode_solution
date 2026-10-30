class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        stone_set = set(stones)
        jumps = {stone: set() for stone in stones}
        jumps[0].add(0)

        for stone in stones:
            for k in jumps[stone]:
                for next_k in (k - 1, k, k + 1):
                    landing = stone + next_k
                    if next_k > 0 and landing in stone_set:
                        if landing == stones[-1]:
                            return True
                        jumps[landing].add(next_k)

        return False
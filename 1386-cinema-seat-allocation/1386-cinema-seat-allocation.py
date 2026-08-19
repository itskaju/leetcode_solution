class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict

        mp = defaultdict(int)

        # store seats using bitmask
        for r, c in reservedSeats:
            if 2 <= c <= 9:   # only useful seats
                mp[r] |= (1 << c)

        # rows without reservations → 2 families each
        total = (n - len(mp)) * 2

        for mask in mp.values():

            left  = (mask & ((1<<2)|(1<<3)|(1<<4)|(1<<5))) == 0
            right = (mask & ((1<<6)|(1<<7)|(1<<8)|(1<<9))) == 0
            mid   = (mask & ((1<<4)|(1<<5)|(1<<6)|(1<<7))) == 0

            if left:
                total += 1
            if right:
                total += 1
            elif not left and mid:
                total += 1

        return total
class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        s = list(s)

        # tree[node] = (lc, rc, pref, suff, best, length)
        tree = [None] * (4 * n)

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = (c, c, 1, 1, 1, 1)
                return

            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def merge(left, right):
            lc, rc = left[0], right[1]
            length = left[5] + right[5]

            # prefix
            pref = left[2]
            if left[2] == left[5] and left[1] == right[0]:
                pref = left[5] + right[2]

            # suffix
            suff = right[3]
            if right[3] == right[5] and left[1] == right[0]:
                suff = right[5] + left[3]

            # best
            best = max(left[4], right[4])
            if left[1] == right[0]:
                best = max(best, left[3] + right[2])

            return (lc, rc, pref, suff, best, length)

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)

        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            res.append(tree[1][4])

        return res
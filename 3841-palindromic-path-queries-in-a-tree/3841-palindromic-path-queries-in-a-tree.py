class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                      s: str, queries: list[str]) -> list[bool]:
        suneravilo = (n, edges, s, queries)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Iterative DFS builds parent, depth, and Euler tour intervals.
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = len(order)
                order.append(u)
                stack.append((u, p, 1))

                for v in graph[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = len(order) - 1

        # Binary lifting table for LCA.
        levels = n.bit_length()
        up = [parent]

        for _ in range(1, levels):
            prev = up[-1]
            up.append([
                prev[prev[u]] if prev[u] != -1 else -1
                for u in range(n)
            ])

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            for k in range(levels - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return parent[a]

        # Fenwick tree supporting range-XOR updates and point queries.
        fenwick = [0] * (n + 1)

        def toggle(index: int, mask: int) -> None:
            index += 1
            while index <= n:
                fenwick[index] ^= mask
                index += index & -index

        def range_xor(left: int, right: int, mask: int) -> None:
            toggle(left, mask)
            if right + 1 < n:
                toggle(right + 1, mask)

        def point_query(index: int) -> int:
            result = 0
            index += 1
            while index:
                result ^= fenwick[index]
                index -= index & -index
            return result

        chars = [ord(c) - ord('a') for c in s]

        # Prefix masks from the root, using the initial characters.
        base_prefix = [0] * n
        for u in order:
            p = parent[u]
            parent_mask = base_prefix[p] if p != -1 else 0
            base_prefix[u] = parent_mask ^ (1 << chars[u])

        answers = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = ord(parts[2]) - ord('a')

                delta = (1 << chars[u]) ^ (1 << new_char)
                if delta:
                    # This node is in the prefix of each node in its subtree.
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = new_char

            else:  # "query u v"
                u = int(parts[1])
                v = int(parts[2])
                ancestor = lca(u, v)

                prefix_u = base_prefix[u] ^ point_query(tin[u])
                prefix_v = base_prefix[v] ^ point_query(tin[v])
                path_mask = prefix_u ^ prefix_v ^ (1 << chars[ancestor])

                # A palindrome permutation allows at most one odd-count letter.
                answers.append((path_mask & (path_mask - 1)) == 0)

        return answers
# python3

import sys


class DisjointSet(object):
    """Simulates a sequence of merge operations with tables in a database.
    Samples:
    >>> s = DisjointSet(5, [1, 1, 1, 1, 1])
    >>> s.merge(3, 5)
    >>> print(s.get_max_lines())
    2
    >>> s.merge(2, 4)
    >>> print(s.get_max_lines())
    2
    >>> s.merge(1, 4)
    >>> print(s.get_max_lines())
    3
    >>> s.merge(5, 4)
    >>> print(s.get_max_lines())
    5
    >>> s.merge(5, 3)
    >>> print(s.get_max_lines())
    5
    >>> # Explanation:
    >>> # In this sample, all the tables initially have exactly 1 row of data.
    >>> # Consider the merging operations:
    >>> # 1. All the data from the table 5 is copied to table number 3.
    >>> # Table 5 now contains only a symbolic link to table 3, while table 3
    >>> # has 2 rows. 2 becomes the new maximum size.
    >>> # 2. 2 and 4 are merged in the same way as 3 and 5.
    >>> # 3. We are trying to merge 1 and 4, but 4 has a symbolic link pointing
    >>> # to 2, so we actually copy all the data from the table number 2 to
    >>> # the table number 1, clear the table number 2 and put a symbolic link
    >>> # to the table number 1 in it. Table 1 now has 3 rows of data,
    >>> # and 3 becomes the new maximum size.
    >>> # 4. Traversing the path of symbolic links from 4 we have 4 → 2 → 1,
    >>> # and the path from 5 is 5 → 3. So we are actually merging tables
    >>> # 3 and 1. We copy all the rows from the table number 1 into the table
    >>> # number 3, and now the table number 3 has 5 rows of data, which is
    >>> # the new maximum.
    >>> # 5. All tables now directly or indirectly point to table 3, so all
    >>> # other merges won’t change anything.
    >>>
    >>> s = DisjointSet(6, [10, 0, 5, 0, 3, 3])
    >>> s.merge(6, 6)
    >>> print(s.get_max_lines()
    10
    >>> s.merge(6, 5)
    >>> print(s.get_max_lines())
    10
    >>> s.merge(5, 4)
    >>> print(s.get_max_lines())
    10
    >>> s.merge(4, 3)
    >>> print(s.get_max_lines())
    11
    >>>
    >>> # Explanation:
    >>> # In this example tables have different sizes.
    >>> # Let us consider the operations:
    >>> # 1. Merging the table number 6 with itself doesn’t change anything,
    >>> # and the maximum size is 10 (table number 1).
    >>> # 2. After merging the table number 5 into the table number 6,
    >>> # the table number 5 is cleared and has size 0, while the table number 6
    >>> # has size 6. Still, the maximum size is 10.
    >>> # 3. By merging the table number 4 into the table number 5, we actually
    >>> # merge the table number 4 into the table number 6 (table 5 now contains
    >>> # just a symbolic link to table 6), so the table number 4 is cleared and
    >>> # has size 0, while the table number 6 has size 6.
    >>> # Still, the maximum size is 10.
    >>> # 4. By merging the table number 3 into the table number 4, we actually
    >>> # merge the table number 3 into the table number 6 (table 4 now contains
    >>> # just a symbolic link to table 6), so the table number 3 is cleared and
    >>> # has size 0, while the table number 6 has size 11,
    >>> # which is the new maximum size.
    """
    def __init__(self, n, lines):
        """Initializes a set for given n elements.
        Initially, the set consists of one element which is pointing to itself.
        Also during initialization the rank(tree's height) is assigned to 1
        for each set."""

        self.n = n
        self.lines = [0] + lines
        self.rank = [0] * (n + 1)
        self.parent = list(range(0, n + 1))
        self.max = max(self.lines)

    def get_parent(self, x):
        """Finds a set id (root of the tree) for element x and compresses path.
        """
        parents_to_update = []

        # Find root.
        root = x
        while root != self.parent[root]:
            parents_to_update.append(self.parent[root])
            root = self.parent[root]

        # Compress path.
        for i in parents_to_update:
            self.parent[i] = root

        return root

    def merge(self, dest, src):
        """Unions tables.
        During union updates rank's(tree's height) array."""
        src_root = self.get_parent(src)
        dest_root = self.get_parent(dest)

        # Means the sets have been merged already.
        if src_root == dest_root:
            return

        if self.rank[src_root] >= self.rank[dest_root]:
            self.parent[src_root] = dest_root
        else:
            self.parent[dest_root] = src_root
            if self.rank[src_root] == self.rank[dest_root]:
                self.rank[src_root] += 1

        self.lines[dest_root] += self.lines[src_root]
        self.lines[src_root] = 0

        if self.max < self.lines[dest_root]:
            self.max = self.lines[dest_root]

    def get_max_lines(self):
        return self.max


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    ds = DisjointSet(n, lines)
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        ds.merge(destination, source)
        print(ds.get_max_lines())
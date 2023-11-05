import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = collections.defaultdict(list)

        for s in strs:
            countmap = [0] * 26
            for c in s:
                countmap[ord(c) - ord('a')] += 1

            hmap[tuple(countmap)].append(s)

        return list(hmap.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["ab", "ba"]))
    print(Solution().groupAnagrams(["a"]))


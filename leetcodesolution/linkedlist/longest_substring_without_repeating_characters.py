class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        longest = left = 0

        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(char)
            longest = max(longest, right - left + 1)
        return longest



    def length_of_longest_substring(self, s):
        char_index_map = {}
        longest = 0
        left = 0  # Left index of the sliding window

        for right, char in enumerate(s):
            # If the character is already in the map and its index is within the current window
            if char in char_index_map and char_index_map[char] >= left:
                # Move the left side of the window to the right of this character's last occurrence
                left = char_index_map[char] + 1
            # Update the last seen index of the character
            char_index_map[char] = right
            # Update the length of the longest substring
            longest = max(longest, right - left + 1)

        return longest

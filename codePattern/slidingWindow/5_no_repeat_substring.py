
def no_repeat_substring(strs:str)->int:

    """
    Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
    
    Time Complexity: O(n) because steps for finding the length of distinct character increase as the data grow
    Space Complexity: O(1) because constant alphabet characters is only 26 distinct letters. 
    """
    right_char = ""
    sub_len = 0
    str_freq = {}
    start_window = 0

    for end_window, char in enumerate(strs):

        if char in str_freq:

            # update start_window to recent index of duplicated character
            start_window = max(end_window, str_freq[char])

        # get char as key and end_window as a vlue for recent key
        str_freq[char] = end_window

        # update recent max sub length and add one because we start with 0
        sub_len = max(sub_len, end_window - start_window + 1)

    

    return sub_len

strs = "aabccbb"
strs = "abbbb"
print( no_repeat_substring(strs))

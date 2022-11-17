
def longest_substring_with_k_distinct(strs:str, K:int)->int:
    longest_substring = 0
    tempfreq = {}
    start_window = 0
    end_window = 0

    for index in range(len(strs)):

        # initialize and count the distinct character 
        if strs[index] not in tempfreq:
            tempfreq[strs[index]] = 0
        tempfreq[strs[index]] += 1

        end_window = index

        # shrink the window if index is longer than the K size
        while len(tempfreq) > K :
            # update the longest sub string 
            # eliminate the duplicate of each character 
            tempfreq[strs[index]] -= 1

            # eliminate each char if reach zero
            if tempfreq[strs[index]] == 0:
                del tempfreq[strs[index]]

            # start shrinking the window 
            start_window += 1
        longest_substring = max(longest_substring, end_window - start_window + 1)
    return longest_substring
strs = "araaci"
K = 2
print(longest_substring_with_k_distinct(strs, K))
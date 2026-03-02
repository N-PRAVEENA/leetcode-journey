class Solution(object):
    def numDifferentIntegers(self, word):
        nums = []
        i = 0

        while i < len(word):
            temp = ''

            # Collect continuous digits
            while i < len(word) and word[i].isnumeric():
                temp += word[i]
                i += 1

            # If number found, remove leading zeros
            if temp:
                temp = temp.lstrip('0')
                nums.append(temp)

            i += 1

        return len(set(nums))
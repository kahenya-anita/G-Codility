# You are given a string S, which consists entirely of decimal digits (0−9). Using digits from S, create a palindromic number with the largest possible decimal value. You should use at least one digit and you can reorder the digits. A palindromic number remains the same when its digits are reversed; for instance, "7", "44" or "83238". Any palindromic number you create should not, however, have any leading zeros, such as in "0990" or "010".

# For example, decimal palindromic numbers that can be created from "8199" are: "1", "8", "9", "99", "919" and "989". Among them, “989” has the largest value.

# Write a function:

# def solution(S)

# that, given a string S of N digits, returns the string representing the palindromic number with the largest value.

# Examples:

# 1. Given "39878", your function should return "898".

# 2. Given "00900", your function should return "9".

# 3. Given "0000", your function should return "0".

# 4. Given "54321", your function should return "5".

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# string S is made only of digits (0−9).

def solution(S):
    # Count the frequency of each digit
    digit_count = [0] * 10
    for digit in S:
        digit_count[int(digit)] += 1

    # Build the left half of the palindrome
    left_half = []
    middle = ""
    
    # Start from 9 and work our way down
    for digit in range(9, -1, -1):
        # Skip leading zeros
        if not left_half and digit == 0:
            continue
        
        # Add pairs of digits to the left half
        pairs = digit_count[digit] // 2
        left_half.extend([str(digit)] * pairs)
        digit_count[digit] -= pairs * 2
        
        # If we haven't found a middle digit yet and there's an odd count
        if not middle and digit_count[digit] > 0:
            middle = str(digit)

    # Construct the full palindrome
    result = ''.join(left_half) + middle + ''.join(left_half[::-1])
    
    # Handle the case where all digits were zero
    return result if result else "0"

# Test cases
print(solution("39878"))  # Should return "898"
print(solution("00900"))  # Should return "9"
print(solution("0000"))   # Should return "0"
print(solution("54321"))  # Should return "5"
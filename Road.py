# You are given a description of a two-lane road in which two strings, L1 and L2, respectively represent the first and the second lane, each lane consisting of N segments of equal length.

# The K-th segment of the first lane is represented by L1[K] and the K-th segment of the second lane is represented by L2[K], where '.' denotes a smooth segment of road and 'x' denotes a segment containing potholes.

# Cars can drive over segments with potholes, but it is rather uncomfortable. Therefore, a project to repair as many potholes as possible was submitted. At most one contiguous stretch of each lane may be repaired at a time. For the time of reparation those stretches will be closed to traffic.

# How many road segments with potholes can be repaired given that the road must be kept open (in other words, stretches of roadworks must not prevent travel from one end of the road to the other)?

# Write a function:

# int solution(char *L1, char *L2);

# that, given two strings L1 and L2 of length N, returns the maximum number of segments with potholes that can be repaired.

# Examples:

# 1. Given L1 = "..xx.x." and L2 = "x.x.x..", your function should return 4. It is possible to repair three potholes in the first lane and the first pothole in the second lane without closing the road to traffic.

# Example test. L1 = "..xx.x.", L2 = "x.x.x..".

# 2. Given L1 = ".xxx...x" and L2 = "..x.xxxx", your function should return 6.

# Second example test. L1 = ".xxx...x", L2 = "..x.xxxx".

# 3. Given L1 = "xxxxx" and L2 = ".x..x", your function should return 5.

# Third example test. L1 = "xxxxx", L2 = ".x..x".

# 4. Given L1 = "x...x" and L2 = "..x..", your function should return 2.

# Fourth example test. L1 = "x...x", L2 = "..x..".

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..200,000];
# strings L1 and L2 consist only of the characters "." and/or "x".

def solution(L1, L2):
    N = len(L1)
    
    def longest_repair(lane):
        max_repair = 0
        current_repair = 0
        for segment in lane:
            if segment == 'x':
                current_repair += 1
                max_repair = max(max_repair, current_repair)
            else:
                current_repair = 0
        return max_repair

    # Find the longest repairable stretch in each lane
    repair_L1 = longest_repair(L1)
    repair_L2 = longest_repair(L2)

    # Count total potholes
    total_potholes = L1.count('x') + L2.count('x')

    # If we can repair all potholes in one lane, do it
    if repair_L1 == L1.count('x') or repair_L2 == L2.count('x'):
        return total_potholes

    # Otherwise, we need to find the best non-overlapping repairs
    best_repair = 0
    current_repair_L1 = 0
    current_repair_L2 = 0

    for i in range(N):
        if L1[i] == 'x':
            current_repair_L1 += 1
        else:
            current_repair_L1 = 0

        if L2[i] == 'x':
            current_repair_L2 += 1
        else:
            current_repair_L2 = 0

        best_repair = max(best_repair, current_repair_L1 + repair_L2, repair_L1 + current_repair_L2)

    return min(best_repair, total_potholes)

# Test cases
print(solution("..xx.x.", "x.x.x.."))  # Should return 4
print(solution(".xxx...x", "..x.xxxx"))  # Should return 6
print(solution("xxxxx", ".x..x"))  # Should return 5
print(solution("x...x", "..x.."))  # Should return 2
import math

testCases = int(input())

for i in range(testCases):
    # Get input for case
    n, k = list(map(int, input().split()))
    string = input()

    # Find goodness score
    score = 0

    for j in range(math.floor(n/2)):
        if string[j] != string[(n-1) - (j + 1) + 1]:
            score += 1


    # Print result
    if score == k:
        print('Case #{CaseNumber}: {Operations}'.format(CaseNumber = i + 1, Operations = 0))
    elif score < k:
        print('Case #{CaseNumber}: {Operations}'.format(CaseNumber = i + 1, Operations = k - score))
    else:
        print('Case #{CaseNumber}: {Operations}'.format(CaseNumber = i + 1, Operations = score - k))

[< Back to Python Projects](https://github.com/KrisLloyd/Python#python)

[< Back to Google Kick Start](https://github.com/KrisLloyd/Python/blob/master/GKS/readme.md#about)
***

# Problem

Charles defines the goodness score of a string as the number of indices i such that **S<sub>[i]</sub>≠S<sub>[N−i+1]</sub>** where 1≤*i*≤N/2 (1-indexed). For example, the string CABABC has a goodness score of **2** since S<sub>2</sub>≠S<sub>5</sub> and S<sub>3</sub>≠S<sub>4</sub>.

Charles gave Ada a string **S** of length **N**, consisting of uppercase letters and asked her to convert it into a string with a goodness score of **K**. In one operation, Ada can change any character in the string to any uppercase letter. Could you help Ada find the minimum number of operations required to transform the given string into a string with goodness score equal to **K**?

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow.

The first line of each test case contains two integers **N** and **K**. The second line of each test case contains a string **S** of length **N**, consisting of uppercase letters.


### Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of operations required to transform the given string **S** into a string with goodness score equal to **K**.

### Limits
Memory limit: 1 GB.

1≤T≤100.

0≤K≤N/2.

### Test Set 1
Time limit: 20 seconds.

1≤N≤100.

### Test Set 2
Time limit: 40 seconds.

1≤N≤2×105 for at most 10 test cases.

For the remaining cases, 1≤N≤100.

# Solution

[kGoodnessString.py](./kGoodnessString.py)

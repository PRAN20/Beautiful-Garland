# Beautiful-Garland
- https://www.codechef.com/problems/BEAUTGAR

## Beautiful Garland Problem Code: 
Read problems statements in Hindi, Mandarin Chinese, Russian, Vietnamese and Bengali as well.
There is a garland — a cyclic rope with red and green flowers on it in some order. The sequence of flower colours is described by a string s
; since the rope is cyclic, each two consecutive flowers are adjacent and the first and last flower are also adjacent.

The garland is beautiful if there is no pair of adjacent flowers with identical colours.

You want the garland to be beautiful. To achieve that, you may perform the following operation at most once:

Make two cuts on the rope (not intersecting the flowers), splitting the garland into two parts.
Reverse one of these two parts.
Tie together corresponding endpoints of the two parts, creating one whole garland again.
Can you find out whether it is possible to make the garland beautiful?

## Input
The first line of the input contains a single integer T
 denoting the number of test cases. The description of T
 test cases follows.
The first and only line of each test case contains a single string s
 describing the garland. Each character of s
 is either 'R' or 'G', denoting a red or green flower respectively.
## Output
For each test case, print a single line containing the string "yes" if the garland can be made beautiful or "no" otherwise.

## Constraints
1≤T≤105
2≤|s|≤105
the sum of |s|
 over all test cases does not exceed 106
## Sample Input 1 
 3
RG
RRGG
RR
## Sample Output 1 
yes
yes
no
## Explanation
Example case 1: The garland is already beautiful.

Example case 2: We can cut the garland between flowers 1 and 2 and between flowers 3 and 4. After reversing the part containing flowers 2 and 3 and rejoining, we obtain "RGRG".

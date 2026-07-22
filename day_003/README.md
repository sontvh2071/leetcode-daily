# 36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.



Input: board = </br>
[["5","3",".",".","7",".",".",".","."]</br>
,["6",".",".","1","9","5",".",".","."]</br>
,[".","9","8",".",".",".",".","6","."]</br>
,["8",".",".",".","6",".",".",".","3"]</br>
,["4",".",".","8",".","3",".",".","1"]</br>
,["7",".",".",".","2",".",".",".","6"]</br>
,[".","6",".",".",".",".","2","8","."]</br>
,[".",".",".","4","1","9",".",".","5"]</br>
,[".",".",".",".","8",".",".","7","9"]]</br>

Output: true

Example 2:

Input: board = </br>
[["8","3",".",".","7",".",".",".","."]</br>
,["6",".",".","1","9","5",".",".","."]</br>
,[".","9","8",".",".",".",".","6","."]</br>
,["8",".",".",".","6",".",".",".","3"]</br>
,["4",".",".","8",".","3",".",".","1"]</br>
,["7",".",".",".","2",".",".",".","6"]</br>
,[".","6",".",".",".",".","2","8","."]</br>
,[".",".",".","4","1","9",".",".","5"]</br>
,[".",".",".",".","8",".",".","7","9"]]</br>

Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

 
Discover more
Mathematics

</br>

# 242. Valid Anagram

Given two strings s and t, return true if t is an

of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

</br>

# 409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest

 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

Constraints:

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.


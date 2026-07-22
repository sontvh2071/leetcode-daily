from typing import List, Tuple


class Solution:
    
    # 36 valid Sudoku
    # method 1: use dictionary to store the position of each number, and check if the same number is in the same row, column or box
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        m = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif self.sameRow(m.get(board[i][j], []), i) or self.sameCol(m.get(board[i][j], []), j) or self.sameBox(m.get(board[i][j], []),i, j):
                    return False
                else:
                    f = m.get(board[i][j], [])
                    f.append((i,j))
                    m[board[i][j]] = f
        
        return True
        
    def sameRow(self, l: List[Tuple[int, int]], x: int) -> bool:
        for item in l:
            if item[0] == x:
                return True
        
        return False

    def sameCol(self, l: List[Tuple[int, int]], y: int) -> bool:
        for item in l:
            if item[1] == y:
                return True

        return False
            

    def sameBox(self, l: List[Tuple[int, int]], x: int, y: int) -> bool:
        for item in l:
            if item[0]//3 == x//3 and item[1]//3 == y//3:
                return True
        
        return False
    
    
    # method 2: use three 9x9 boolean matrices to track the presence of each number in each row, column and box
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    boxIndex = (i // 3) * 3 + (j // 3)
                    if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                        return False
                    rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True
        return True
    
    # 242 valid anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m = {}
        for i in range(len(s)):
            m[s[i]] = m.get(s[i], 0) + 1
            m[t[i]] = m.get(t[i], 0) - 1

        return not any(v != 0 for v in m.values())
    
    # 409 longest palindrome
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for char in s:
            m[char] = m.get(char, 0) + 1

        l = 0
        f = False
        for count in m.values():
            if count % 2 == 0:
                l += count
            else:
                l += count - 1
                f = True
        
        return l + 1 if f else l
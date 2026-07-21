# LeetCode Daily

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Daily-FFA116?logo=leetcode&logoColor=black)](https://leetcode.com/)
[![GitHub last commit](https://img.shields.io/github/last-commit/sontvh2071/leetcode-daily)](https://github.com/sontvh2071/leetcode-daily/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/sontvh2071/leetcode-daily)](https://github.com/sontvh2071/leetcode-daily)

A personal repository for practicing **LeetCode problems**, improving **data structures and algorithms**, and preparing for technical interviews using Python.

## Goals

- Solve LeetCode problems consistently.
- Build strong foundations in data structures and algorithms.
- Compare brute-force and optimized approaches.
- Analyze time and space complexity.
- Write clean, readable, and maintainable Python code.
- Track daily learning progress for interview preparation.

## Repository Structure

Each practice day is stored in a separate directory:

```text
leetcode-daily/
├── day_001/
├── day_002/
├── day_003/
├── ...
└── README.md
```

A daily folder may contain:

```text
day_xxx/
├── solution.py      # Python solution
├── test.py          # Optional local test cases
└── README.md        # Optional explanation and notes
```

## Progress

| Day | Solution | Status |
|---:|---|:---:|
| 001 | [View solution](./day_001) | ✅ |
| 002 | [View solution](./day_002) | ✅ |

> The table will be updated as new daily solutions are added.


## Solution Format

For each problem, I aim to document:

- Problem statement or LeetCode link
- Initial idea
- Brute-force approach
- Optimized approach
- Time complexity
- Space complexity
- Important edge cases

Example:

```python
from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        """Return the result for the given input."""
        pass
```

## Running a Solution

Clone the repository:

```bash
git clone https://github.com/sontvh2071/leetcode-daily.git
cd leetcode-daily
```

Find the Python file for a specific day:

```bash
find day_001 -name "*.py"
```

Run it locally when the file includes executable test cases:

```bash
python3 day_001/<file_name>.py
```

## Daily Workflow

```bash
# Create the next daily directory
mkdir -p day_004

# Add a solution
touch day_004/solution.py

# Commit the progress
git add .
git commit -m "feat: add day 004 solution"
git push origin main
```

## Commit Convention

Recommended commit messages:

```text
feat: add day 004 solution
refactor: optimize day 004 solution
test: add edge cases for day 004
docs: update progress table
```

## Notes

These solutions are written for learning and interview preparation. Some problems may include multiple approaches to demonstrate the trade-offs between readability, execution time, and memory usage.

## Author

**Son TVH**

- GitHub: [@sontvh2071](https://github.com/sontvh2071)
- Repository: [leetcode-daily](https://github.com/sontvh2071/leetcode-daily)

---

> Consistency is more important than solving every problem perfectly on the first attempt.

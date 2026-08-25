# Striver's A2Z DSA Sheet — Python Solutions

Personal log of solutions to [Striver's A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course-sheet-2), solved in **Python 3**, as part of my daily DSA practice and interview prep. 
``IF IN FUTURE I FIND BETTER PROBLEM SHEETS, I WILL ADD IT IN THIS REPO AS A NEW DIRECTORY``

Each solution is documented with the approach, time/space complexity, and a link back to the original problem — so this repo doubles as a searchable revision log, not just a code dump.

---

## 📁 Repository Structure

```
striver-a2z-dsa-sheet/
├── README.md
├── 01-Basics/
├── 02-Sorting/
├── 03-Arrays/
│   ├── two_sum_easy.py
│   ├── kadanes_algorithm_medium.py
│   └── README.md
├── 04-Binary-Search/
├── 05-Strings/
├── 06-LinkedList/
├── 07-Recursion-Backtracking/
├── 08-Bit-Manipulation/
├── 09-Stack-Queue/
├── 10-Sliding-Window-Two-Pointer/
├── 11-Heaps/
├── 12-Greedy/
├── 13-Binary-Trees/
├── 14-Binary-Search-Trees/
├── 15-Graphs/
├── 16-Dynamic-Programming/
├── 17-Tries/
└── 18-Advanced-Topics/
```

Each topic folder has its own `README.md` logging every problem solved there (see [boilerplate](#-per-problem-template) below).

---

## 🐍 Conventions

- **Language:** Python 3.11+
- **File naming:** `snake_case`, matching the problem name and difficulty
  ```
  two_sum_easy.py
  merge_intervals_medium.py
  word_ladder_hard.py
  ```
- **Function naming:** Solutions are wrapped in a `Solution` class with a `solve` method (matches LeetCode's own template) so every file has a predictable entry point.
- **Style:** [PEP 8](https://peps.python.org/pep-0008/), type hints where they aid readability, no external dependencies beyond the standard library (`collections`, `heapq`, `bisect`, etc.).
- I MAY ADD OTHER LANGUAGES LIKE JAVA, JS ETC IN FUTURE.

---

## 📊 Progress Tracker

| Topic                          | Solved | Total | Status         |
|---------------------------------|:------:|:-----:|----------------|
| 01. Basics                      | 0      | —     | 🔴 Not Started |
| 02. Sorting                     | 0      | —     | 🔴 Not Started |
| 03. Arrays                      | 0      | —     | 🔴 Not Started |
| 04. Binary Search                | 0      | —     | 🔴 Not Started |
| 05. Strings                     | 0      | —     | 🔴 Not Started |
| 06. Linked List                 | 0      | —     | 🔴 Not Started |
| 07. Recursion & Backtracking     | 0      | —     | 🔴 Not Started |
| 08. Bit Manipulation             | 0      | —     | 🔴 Not Started |
| 09. Stack & Queue                | 0      | —     | 🔴 Not Started |
| 10. Sliding Window / Two Pointer | 0      | —     | 🔴 Not Started |
| 11. Heaps                       | 0      | —     | 🔴 Not Started |
| 12. Greedy                      | 0      | —     | 🔴 Not Started |
| 13. Binary Trees                 | 0      | —     | 🔴 Not Started |
| 14. Binary Search Trees          | 0      | —     | 🔴 Not Started |
| 15. Graphs                      | 0      | —     | 🔴 Not Started |
| 16. Dynamic Programming          | 0      | —     | 🔴 Not Started |
| 17. Tries                       | 0      | —     | 🔴 Not Started |
| 18. Advanced Topics              | 0      | —     | 🔴 Not Started |

*(Update the counts as you go — 🔴 Not Started / 🟡 In Progress / ✅ Complete)*

---

## 📝 Per-Problem Template

Every topic-level `README.md` logs problems in this format:

```markdown
## Two Sum — Easy

**Problem:** Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to `target`.

**Approach:**
Use a hash map to store each number's complement and index while iterating
once through the array — avoids the O(n²) brute-force nested loop.

**Time Complexity:** O(n)
**Space Complexity:** O(n)
**File:** [`two_sum_easy.py`](./two_sum_easy.py)
**Link:** https://leetcode.com/problems/two-sum/
```

---

## ✅ Workflow

1. Solve the problem on LeetCode until accepted.
2. Copy the solution into the matching topic folder using the [Python boilerplate](#-python-boilerplate) below.
3. Log it in that folder's `README.md`.
4. Commit with a descriptive message:
   ```bash
   git add 03-Arrays/two_sum_easy.py
   git commit -m "feat: Add solution for Two Sum (Easy) in Arrays"
   git push origin main
   ```

---

## 🐍 Python Boilerplate

See [`boilerplate.py`](./boilerplate.py) — copy it into a new file for every problem and fill in the blanks.

# Detailed Dry Run Walkthrough

Let's dry run the solution with an example to see exactly how the pointers and hash map change at each step.

### Input:
* `s = "aabacbe"`
* `k = 3`

### Step-by-Step Execution Trace:

| Step (`b`) | Character | `char_map` | Map Size | Condition Checked | `a` (Left) | Window (`s[a:b+1]`) | `max_len` |
|:---:|:---:|:---|:---:|:---|:---:|:---:|:---:|
| **Initial** | - | `{}` | 0 | - | 0 | - | -1 |
| **0** | `'a'` | `{'a': 1}` | 1 | `len == k` (False) | 0 | `"a"` | -1 |
| **1** | `'a'` | `{'a': 2}` | 1 | `len == k` (False) | 0 | `"aa"` | -1 |
| **2** | `'b'` | `{'a': 2, 'b': 1}` | 2 | `len == k` (False) | 0 | `"aab"` | -1 |
| **3** | `'a'` | `{'a': 3, 'b': 1}` | 2 | `len == k` (False) | 0 | `"aaba"` | -1 |
| **4** | `'c'` | `{'a': 3, 'b': 1, 'c': 1}` | 3 | `len == k` (True) -> Length = 5 | 0 | `"aabac"` | **5** |
| **5** | `'b'` | `{'a': 3, 'b': 2, 'c': 1}` | 3 | `len == k` (True) -> Length = 6 | 0 | `"aabacb"` | **6** |
| **6** | `'e'` | `{'a': 3, 'b': 2, 'c': 1, 'e': 1}` | 4 | `len > k` -> **Shrink Triggered** | 0 | `"aabacbe"` | 6 |

### Inside the Shrink Loop (at Step 6):
Because the map size became `4` (which is greater than `k=3`), the `while` loop runs to move pointer `a`:
1. `a = 0`: Remove `s[0]` (`'a'`). Map becomes `{'a': 2, 'b': 2, 'c': 1, 'e': 1}`. Size is still 4. `a` becomes 1.
2. `a = 1`: Remove `s[1]` (`'a'`). Map becomes `{'a': 1, 'b': 2, 'c': 1, 'e': 1}`. Size is still 4. `a` becomes 2.
3. `a = 2`: Remove `s[2]` (`'b'`). Map becomes `{'a': 1, 'b': 1, 'c': 1, 'e': 1}`. Size is still 4. `a` becomes 3.
4. `a = 3`: Remove `s[3]` (`'a'`). Map becomes `{'b': 1, 'c': 1, 'e': 1}` (`'a'` count hit 0, so deleted). Size becomes 3! Loop stops. `a` becomes 4.

### Final Check at Step 6:
* Now `a = 4`, `b = 6`. 
* Map size is exactly 3 (`{'b': 1, 'c': 1, 'e': 1}`).
* New window is `"cbe"`. Current length = `6 - 4 + 1 = 3`. 
* Since 3 is not greater than our `max_len` (6), `max_len` remains **6**.

### Final Output: `6` (Substring: `"aabacb"`)

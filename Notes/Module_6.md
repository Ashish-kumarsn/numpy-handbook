# Module 6 — Shape Manipulation (Part 1)

---

## What even is Shape Manipulation?

Simple baat — data same rehta hai, bas uski **arrangement change hoti hai.**

```python
arr = np.array([1, 2, 3, 4, 5, 6])   # shape (6,)

arr.reshape(2, 3)
# [[1 2 3]
#  [4 5 6]]                           # shape (2,3)
```

1 se 6 wahi hain. Kuch change nahi hua. Bas layout badla.

---

## Why do we even need this?

ML/DL me data ka shape bohot matter karta hai. Model ek specific shape expect karta hai.

- Image load ki → shape `(224, 224, 3)` — but model wants `(1, 224, 224, 3)`
- Dataset hai `(100, 5)` — algorithm wants `(100, 5, 1)`
- Same data. Different shape. Bas itna.

---

## 3 properties yaad rakho

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr.shape   # (2, 3)  → 2 rows, 3 cols — arrangement
arr.size    # 6       → total elements
arr.ndim    # 2       → kitne dimensions hain
```

| Property | Kya batata hai | Example |
|----------|----------------|---------|
| `shape`  | arrangement    | `(2,3)` |
| `size`   | total elements | `6`     |
| `ndim`   | dimensions count | `2`   |

---

## Golden Rule 

> **Reshape tab hi hoga jab total elements same rahein.**

```python
arr = np.arange(24)   # 24 elements

arr.reshape(4, 6)     #   4×6   = 24
arr.reshape(2, 3, 4)  #   2×3×4 = 24
arr.reshape(5, 5)     #   5×5   = 25  → error!
```

Size kabhi nahi badlti — sirf shape aur ndim badalta hai.

---

## One liner summary

> Shape manipulation = same books, different shelf arrangement.


# Part 9: Splitting Arrays

---

## What is Splitting?

Splitting is the **opposite of stacking**.

```
Stacking  : Small Arrays → One Big Array
Splitting : One Big Array → Small Arrays
```

Ek bade array ko chhote pieces me divide karna — that's splitting.

---

## Functions Overview

| Function | Purpose |
|----------|---------|
| `split()` | Equal splits only |
| `array_split()` | Equal OR unequal splits |
| `hsplit()` | Split columns (horizontal) |
| `vsplit()` | Split rows (vertical) |
| `dsplit()` | Split depth (3D arrays) |

---



## 1. split()

Basic splitting function.

**Rule  — Parts must be EQUAL sized.**

If array can't be divided equally → `ValueError` immediately.

Two ways to use it:
- Pass number of parts → `np.split(arr, 2)`
- Pass indices (cut points) → `np.split(arr, [2, 5])`

---

## 2. array_split()

Smarter version of `split()`.

**Allows unequal parts** — no error even if division isn't exact.

Extra elements go into the earlier splits automatically.

> Use this when you're NOT sure if array divides evenly. You'll see this most in real projects.

---

## 3. hsplit() — Horizontal Split

Works on **2D arrays**.

Splits **column-wise** (cuts vertically).

```
1 2 | 3 4
5 6 | 7 8
```

---

## 4. vsplit() — Vertical Split

Works on **2D arrays**.

Splits **row-wise** (cuts horizontally).

```
1 2
3 4
-----
5 6
7 8
```

> Easy trick to remember:
> - **h**split → splits **columns** (like cutting a book page left-right)
> - **v**split → splits **rows** (like cutting a book page top-bottom)

---

## 5. dsplit() — Depth Split

Works on **3D arrays**.

Splits along the third dimension (depth).

Used with images, videos, 3D tensors.

---

## Important Notes

- Output is always a **list of arrays** → access with `parts[0]`, `parts[1]`
- Splitting usually returns **views** (not copies) → memory efficient
- `split()` → strict, use only when sure of equal division
- `array_split()` → flexible, safe default choice




## Interview Questions

**Q1. Difference between `split()` and `array_split()`?**
> `split()` needs equal parts → error if not possible.
> `array_split()` handles unequal parts automatically.

**Q2. Which to use when elements aren't perfectly divisible?**
> Always use `array_split()`.

**Q3. What does `hsplit()` split — rows or columns?**
> Columns (horizontal cut).





Module code file :

reshape()
flatten()
ravel()
transpose()
expand_dims()
Stacking Arrays
Splitting Arrays

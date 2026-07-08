# Module 2 — Array Creation

NumPy provides several built-in functions to create `ndarray` objects — from existing data, filled with constants, or as sequences of numbers.

---

## 1. `np.array()`

Creates an `ndarray` from existing data (like a Python list).

```python
np.array([1, 2, 3])
```

---

## 2. `np.zeros()`

Creates an array filled with **zeros**.

```python
np.zeros((3, 4))
```

- **Default datatype:** `float64`
- Can be changed using `dtype`:

```python
np.zeros((3, 4), dtype=np.int32)
```

---

## 3. `np.ones()`

Creates an array filled with **ones**.

```python
np.ones((2, 3))
```

---

## 4. `np.full()`

Creates an array filled with **any constant** value.

```python
np.full((3, 3), 7)
```

---

## 5. `np.arange()`

Similar to Python's `range()`, but returns an `ndarray`.

**Syntax:**

```python
np.arange(start, stop, step)
```

**Example:**

```python
np.arange(2, 20, 3)
```

**Output:**

```
2 5 8 11 14 17
```



## 6. `np.linspace()`

Creates **equally spaced numbers** between a start and stop value.

**Syntax:**

```python
np.linspace(start, stop, number_of_values)
```

**Example:**

```python
np.linspace(0, 100, 10)
```

### Difference: `arange()` vs `linspace()`

| Function | Uses |
|-----------|------|
| `arange()` | Step size |
| `linspace()` | Number of samples |

---

## 7. `np.eye()`

Creates an **identity matrix**.

- Can create **rectangular** matrices too.

```python
np.eye(3, 4)
```

---

## 8. `np.identity()`

Creates a **square identity matrix only**.

```python
np.identity(4)
```

### Difference: `eye()` vs `identity()`

| Function | Shape |
|-----------|-------|
| `eye()` | Rectangular or Square |
| `identity()` | Square only |

---

## 9. `np.empty()`

Allocates memory **without initialization**.

```python
np.empty((3, 3))
```

- Output contains **arbitrary values** already present in memory.
- Used when data will be **overwritten immediately**.
- **Faster** than `zeros()` because it doesn't initialize the memory.

---

## Default Data Type

Functions like:

```python
zeros()
ones()
full()
```

default to **`float64`**.

Datatype can be changed using `dtype=`:

```python
np.zeros((5, 5), dtype=np.int16)
```

---

## Important Formulas

```
nbytes = size × itemsize
```

```
shape = (Number of Rows, Number of Columns, ...)
```


---

## Quick Reference Table

| Function | Purpose | Example |
|-----------|----------|----------|
| `np.array()` | Create array from data | `np.array([1,2,3])` |
| `np.zeros()` | Array filled with 0s | `np.zeros((3,4))` |
| `np.ones()` | Array filled with 1s | `np.ones((2,3))` |
| `np.full()` | Array filled with constant | `np.full((3,3), 7)` |
| `np.arange()` | Sequence using step size | `np.arange(2,20,3)` |
| `np.linspace()` | Sequence using sample count | `np.linspace(0,100,10)` |
| `np.eye()` | Identity (rect. or square) | `np.eye(3,4)` |
| `np.identity()` | Identity (square only) | `np.identity(4)` |
| `np.empty()` | Uninitialized array | `np.empty((3,3))` |
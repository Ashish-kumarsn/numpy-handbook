# Module 1 — NumPy `ndarray` (N-dimensional Array)

Everything in NumPy revolves around one core object:

```python
numpy.ndarray
```

It is NumPy's **primary data structure**.

---

## Meaning of `ndarray`

**N = Any Number of Dimensions**

| Dimension | Example | Description |
|-----------|---------|-------------|
| 0D | `5` | A single scalar value |
| 1D | `[1, 2, 3]` | A vector / list of numbers |
| 2D | `[[1, 2], [3, 4]]` | A matrix (rows & columns) |
| 3D | Stack of matrices | e.g. a color image (H × W × Channels) |
| 4D+ | Used in AI/ML | e.g. batch of RGB images |

**Example (4D):** Batch of RGB Images

```python
(batch, height, width, channels)
```

---

## Creating an `ndarray`

```python
import numpy as np

arr = np.array([1, 2, 3])
```

### Checking Type

```python
type(arr)
```

**Output:**

```python
<class 'numpy.ndarray'>
```

> Note: This is **not** a Python `list` — it's a NumPy `ndarray`.

---

## Important `ndarray` Properties

### 1. `ndim` — Number of Dimensions

```python
arr = [1, 2, 3]
```

**Output:** `1`

---

### 2. `shape` — Number of Elements in Each Dimension

```python
arr = [[1, 2, 3],
       [4, 5, 6]]
```

**Output:** `(2, 3)`

**Meaning:**
- 2 Rows
- 3 Columns

---

### 3. `size` — Total Number of Elements

```python
2 × 3 = size = 6
```

---

### 4. `dtype` — Data Type of Every Element

Common types:

```
int8
int16
int32
int64
float32
float64
```

---

### 5. `itemsize` — Memory Occupied by One Element

| Data Type | Size |
|-----------|------|
| `int8`  | 1 Byte  |
| `int16` | 2 Bytes |
| `int32` | 4 Bytes |
| `int64` | 8 Bytes |

---

### 6. `nbytes` — Total Memory Occupied by Array

**Formula:**

```
nbytes = size × itemsize
```

**Example:**

```
4 elements, dtype = int32
Memory = 4 × 4 = 16 Bytes
```

---

## Internal Representation of `ndarray`

Conceptually:

```
ndarray Object
      │
      ▼
   Metadata
      ├── Shape
      ├── dtype
      └── Dimensions
      │
      ▼
Pointer to Data
      │
      ▼
  Raw Memory
  [10, 20, 30, 40]
```

> **Important:** Metadata and actual data are stored **separately**.

---

## Why is Shape Stored?

Raw memory:

```
1 2 3 4 5 6
```

This same raw memory block can represent different shapes:

- `(6,)`
- `(2, 3)`
- `(3, 2)`

 **Shape tells NumPy how to interpret the raw memory.**

---

## Memory Formula (Summary)

```
Total Memory = Number of Elements × Memory per Element
```

---

## Quick Reference Table

| Property | Meaning | Example |
|-----------|----------|----------|
| `ndim` | Number of dimensions | `1` |
| `shape` | Shape of array (rows, cols, ...) | `(2, 3)` |
| `size` | Total number of elements | `6` |
| `dtype` | Data type of elements | `int32` |
| `itemsize` | Bytes per element | `4` |
| `nbytes` | Total bytes used | `16` |
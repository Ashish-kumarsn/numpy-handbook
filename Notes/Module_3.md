# INDEXING AND SLICING

## INDEXING

it is necessary for accesing the element of the array we have created .

```python
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0]) -> 10
arr[2]=100 -> modify the value of 3rd element to 100
```

### Negative indexing

```
-5 -4 -3 -2 -1

  ↓

10 20 30 40 50
```

arr[-1] -> 50 , usefull when length of array is not known

## SLICING

Used to grab the specific chunk of array without copying the whole elements.

Syntex -> `[start:stop:steps]`

(view example code -> Slicing.py )

also , start -> included and stop -> excluded

## VIEW AND COPY

### VIEW

When we do something like this

```python
arr = np.array([1,2,3,4,5])
newarr = arr
```

then many people think that this will create a new array but it's not
Both variables point to the same ndarray.
No new memory was created.

When we do , newarr[0]=100 then the value of arr will also change .

Also when we do slicing then also new memory is not allocated -> Slicing return a view not copy

```python
Slice=arr[1:2]
```

, this will just start reading the element not creating a copy .

### COPY

To copy an array with the new memory we write:

```python
arr = np.array([1,2,3])
copy_arr = arr.copy()
```

now copy_arr[0]=100, will update only the copy_arr not the original array

## BOOLEAN INDEXING

### What is Boolean Indexing?

Boolean Indexing is a technique used to select elements based on a condition instead of their position (index).

Unlike normal indexing, we do not specify indices. Instead, we provide a condition,
and NumPy returns all elements that satisfy that condition.

### Why do we need Boolean Indexing?

Suppose

```python
arr = np.array([10,20,30,40,50])
```

Need:

> Select all numbers greater than **25**.

Using normal indexing or slicing is difficult because we don't know the positions of the required elements.

Boolean Indexing solves this problem.

### How Boolean Indexing Works

It happens in two steps.

**Step 1: Create a Boolean Array**

```python
arr = np.array([10,20,30,40,50])

arr > 25
```

Output

```
[False False True True True]
```

Each element is compared with the condition.

10 > 25 → False

20 > 25 → False

30 > 25 → True

40 > 25 → True

50 > 25 → True

**Step 2: Filter the Array**

```python
arr[arr > 25]
```

```
[30 40 50]
```

NumPy keeps only the elements whose corresponding Boolean value is True.

## Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or Equal |
| `<=`     | Less than or Equal    |
| `==`     | Equal                 |
| `!=`     | Not Equal             |

### Greater Than

```python
arr[arr > 25]
```

```
[30 40 50]
```

### Less Than

```python
arr[arr < 30]
```

Output

```
[10 20]
```

### Equal To

```python
arr[arr == 40]
```

```
[40]
```

### Not Equal

```python
arr[arr != 20]
```

Output

```
[10 30 40 50]
```

### Greater Than or Equal

```python
arr[arr >= 30]
```

Output

```
[30 40 50]
```

### Less Than or Equal

```python
arr[arr <= 20]
```

Output

```
[10 20]
```

## Boolean Indexing on 2D Arrays

```python
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

arr[arr > 50]
```

Output

```
[60 70 80 90]
```

**Important**

Even if the input array is 2D, the filtered result is returned as a **1D array**.

## Combining Multiple Conditions

### AND (`&`)

Need numbers between **20** and **50**.

```python
arr[(arr > 20) & (arr < 50)]
```

Output

```
[30 40]
```

### OR (`|`)

Need numbers less than **20** or greater than **40**.

```python
arr[(arr < 20) | (arr > 40)]
```

Output

```
[10 50]
```

### NOT (`~`)

Need everything except numbers greater than **30**.

```python
arr[~(arr > 30)]
```

Output

```
[10 20 30]
```

### Why don't we use `and`, `or`, and `not`?

Python keywords

```
and
or
not
```

work only with **single Boolean values**.

NumPy performs comparisons element by element, so it uses

| Operator | Meaning          |
| -------- | ---------------- |
| `&`      | Element-wise AND |
| `\|`     | Element-wise OR  |
| `~`      | Element-wise NOT |

**Always put each condition inside parentheses.**

Correct

```python
(arr > 20) & (arr < 50)
```

Incorrect

```python
arr > 20 & arr < 50
```

## Does Boolean Indexing Return a View or a Copy?

Boolean Indexing returns a **Copy**.

```python
selected = arr[arr > 20]
```

Changing

```
selected
```

does **not** modify the original array.

## Real AI Applications

**Data Cleaning**

Remove invalid values.

```python
clean_data = data[data >= 0]
```

**Machine Learning**

Keep only confident predictions.

```python
predictions = prob[prob > 0.90]
```

**Computer Vision**

Select bright pixels.

```python
bright_pixels = image[image > 200]
```

Boolean Indexing is the foundation of DataFrame filtering.

Example:

```python
students[students["Marks"] > 90]
```

## Difference Between Indexing Techniques

| Technique         | Selects Using     | Returns         |
| ------------------ | ------------------ | ---------------- |
| Normal Indexing    | Single Index       | Single Element   |
| Slicing            | Continuous Range   | View             |
| Fancy Indexing     | List of Indices    | Copy             |
| Boolean Indexing   | Condition          | Copy             |

## NP.WHERE

```python
np.where(condition, true_value, false_value)
```

Works like an element-wise IF-ELSE.
It return a copy not view

Eg.

```python
marks = np.array([35,80,55,20,95])

result = np.where(marks >= 40, "Pass", "Fail")

print(result)   -> ['Fail' 'Pass' 'Pass' 'Fail' 'Pass']
```
# hackerrank-python
Python Hackerrank training exercises

## palindromic_triangle.py
**Objetive:** This exercise must be print a palindromic number triangle for a entered integer number. 
**Input/Output example:**

If we type n = 7:
 7

We need to get:
 1
 121
 12321
 1234321
 123454321
 12345654321
 1234567654321

**Requirements:**
The difficulty appears when the program only can  contain from one to two lines of code.

**Context:**
The use of "lambda functions" in his recursive mode, can be useful here, and there is an mathematical tip: the use of multiplication of series of numbers 1, 11, 111, 1111, 11111, ..., from the number theory. This type of multiplication has a behavior like the palindromic objective triangle.

```python
for count, line in enumerate(map((serie:=lambda x: pow(10,x-1) + serie(x-1) if x>1 else x),range(1,int(input())+1)),1): print (line*line)
```
**Code description:**
We iterate in a range() from 1 to input()+1, we added 1 to avoid the starting from 0, and it is needed to convert the input to int. 

This range is used in a map function that save the generated serie. 

To every number from the range, we apply a recursive lambda function, named *serie*, in every iteration we do the math operation (10 elevated to range-iterated - 1), and add the call to the next recursive execution for the next range-iterated - 1, until to get 0. 

The iteration of the pow() + the serie(x-1) generate an 1, 11, 111, 1111, ..., serie that if we multiply by self we obtain the stepped serie of numbers (number theory).




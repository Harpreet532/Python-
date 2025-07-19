# numpy_tutorial.py
# 🧮 NumPy Tutorial: Learn NumPy by Writing and Running Code

# Import NumPy
import numpy as np

# ---------------------------------------------
# 1. Creating Arrays
# ---------------------------------------------

# Create a 1D array from a list
a=np.array([1,2,3])
print("1D Array:",a)

# Create a 2D array (matrix)
b=np.array([[1,2],[3,4]])
print(f"2D Array:\n",b)

# ---------------------------------------------
# 2. Array Properties
# ---------------------------------------------
print("Sahpe:",a.shape)
print("Dimensions:",a.ndim)
print("Data type:",a.dtype)
print("Total elements:",a.size)

# ---------------------------------------------
# 3. Special Arrays
# ---------------------------------------------
#to make a zero matrix of order 2*3
print("Zeros:\n",np.zeros((2,3)))
#To make a matrix of order 3*3 with all entries 1
print("Ones:\n",np.ones((3,3)))
#To make a 2*2 matrix with all entries 7
print("Full with 7s:\n",np.full((2,2),7))
#To make an identity matrix
print("Identity Matrix:\n",np.eye(3))
#To print the numbers between given 2 numbers excluding the end number, at given step size
print("Range with step:\n",np.arange(0,10,2))
#To print required number of entries between two numbers which are evenly spaced
print("Evenly spaced:\n",np.linspace(0,2,5))

# ---------------------------------------------
# 4. Reshaping & Flattening
# ---------------------------------------------

arr=np.arange(1,7)
reshaped=arr.reshape((2,3))

print("Reshaped 2X3:\n",reshaped)
print("Flattened:",reshaped.flatten())

# ---------------------------------------------
# 5. Indexing & Slicing
# ---------------------------------------------
matrix=np.array([[10,20,30],[40,50,60]])
print("matrix:\n",matrix[:,:])
print("Element at row 1,col 2:",matrix[1,2])
print("Second column:",matrix[:,1])
print("Submatrix (rows 0-1,cols 1-2):\n",matrix[0:2,1:3])


# ---------------------------------------------
# 6. Element-wise Operations
# ---------------------------------------------
x=np.array([1,2,3])
y=np.array([4,5,6])
print("Add:",x+y)
print("Multiply:",x*y)
print("Square root:",np.sqrt(x))
print("Exponential:",np.exp(x))
print("Log:",np.log(x))

# ---------------------------------------------
# 7. Matrix Multiplication
# ---------------------------------------------
m1=np.array([[1,2],[3,4]])
m2=np.array([[2,0],[1,3]])
product=np.dot(m1,m2)
print("Matrix Product:\n",product)

# ---------------------------------------------
# 8. Aggregate Functions
# ---------------------------------------------
stats = np.array([[5, 10, 15], [20, 25, 30]])
print("Sum:",stats.sum())
print("Mean:",stats.mean())
print("Std Dev:",stats.std())
print("Min:",stats.min())
print("Max:",stats.max())
print("Column-wise sum:",stats.sum(axis=0))
print("Row-wise sum:",stats.sum(axis=1))

# ---------------------------------------------
# 9. Boolean Filtering
# ---------------------------------------------
data=np.array([10,20,30,40,50])
mask=data>30
print("Mask:",mask)
print("Filtered Data:",data[mask])

# ---------------------------------------------
# 10. Random Numbers
# ---------------------------------------------
print("Random float[0,1]:\n",np.random.rand(2,3))
print("Standard normal:\n",np.random.rand(3))
print("Random intergers:\n",np.random.randint(1,10,5))

# ---------------------------------------------
# 11. Useful Functions
# ---------------------------------------------
print("Unique:",np.unique([1,2,2,3,3,3]))
print("Sorted:",np.sort([5,3,1,2]))
print("Clipped (0 to 5):",np.clip([1,5,10],0,5))

# ---------------------------------------------
# 12. Mini Project: Student Score Analysis
# ---------------------------------------------
# Simulate test scores for 5 students across 3 tests
scores=np.array([
    [88,92,85],
    [78,81,79],
    [90,87,88],
    [69,72,70],
    [95,94,96]
])

# Average score per student (row-wise)
student_avg=scores.mean(axis=1)

# Average score per test (column-wise)
test_avg=scores.mean(axis=0)

# Find students with average > 85
high_performers=scores[student_avg>85]

print("Student Avengers:",student_avg)
print("Test Averages:",test_avg)
print("High Performing Students:\n",high_performers)
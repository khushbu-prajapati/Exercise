import numpy as np

data = np.genfromtxt(
    "central_India_rainfall_act_dep_1901_2015.csv",
    delimiter=",",
    skip_header=1,
    dtype = [
        ("year", "i4"),
        ("actual_rainfall_jun", "f8"),
        ("actual_rainfall_jul", "f8"),
        ("actual_rainfall_aug", "f8"),
        ("actual_rainfall_sep", "f8"),
        ("actual_rainfall_jun_sep", "f8"),
        ("departure_percentage_jun", "f8"),
        ("departure_percentage_jul", "f8"),
        ("departure_percentage_aug", "f8"),
        ("departure_percentage_sep", "f8"),
        ("departure_percentage_jun_sep", "f8")
    ],
    encoding="utf-8"
)
# print(data)

#1). Print the type() of the loaded NumPy object.
print(f"Type Of Data: {type(data)}")

# 2).Print its shape, ndim, size, and dtype. 
print(f"Shape of Data: {data.shape}")
print(f"Dimension of Data: {data.ndim}")
print(f"Size of Data: {data.size}")
print(f"Data Type of data: {data.dtype}")

# 3).Print the first 5 records
print(f"First 5 Records: {data[:5]}")

# 4).Print the last 5 records. 
print(f"Last 5 Records: {data[-5:]}")

# 5).Access the rainfall record at index 0. 
print(f"Index 0: {data[0]}")

# 6).Access the rainfall record at index 5. 
print(f"Index 5: {data[5]}")

# 7).Access the last rainfall record using negative indexing. 
print(f"Last Record Using Negative Index: {data[-1]}")

# 8).Slice and display the first 10 records. 
print(f"First 10 Records: {data[:10]}")

# 9).Slice and display records from index 10 to 20. 
print(f"Data From 10 to 20: {data[10:21]}")

# 10).Display every second record using slicing. 
print(f"Every Second Record: {data[::2]}")

# 11).Display the records in reverse order. 
print(f"Reverce Order: {data[::-1]}")

# 12).Extract the annual rainfall column into a separate NumPy array. 
annual_rainfall = data["actual_rainfall_jun_sep"].copy()
print("Annual Rainfall:", annual_rainfall)

# 13).Add 100 to every value in the annual rainfall array. 
add_annual_rainfall = annual_rainfall + 100
print(f"Add 100: {add_annual_rainfall}")

# 14).Multiply every annual rainfall value by 2. 
multiply_annual_rainfall = annual_rainfall * 2
print(f"Multiply by 2: {multiply_annual_rainfall}")

# 15).Divide every annual rainfall value by 2. 
divide_annual_rainfall = annual_rainfall / 2
print(f"Divide by 2: {divide_annual_rainfall}")

# 16).Calculate the difference between the rainfall of two selected years.
rainfall_1907 = annual_rainfall[7]
rainfall_1908 = annual_rainfall[8] 

diff = rainfall_1907 - rainfall_1908
print("Difference:", diff)

# 17).Calculate the average annual rainfall using np.mean().
avg_rainfall = np.mean(annual_rainfall) 
print(f"Mean: {avg_rainfall}")

# 18).Find the highest annual rainfall using np.max(). 
max_rainfall = np.max(annual_rainfall) 
print(f"Max: {max_rainfall}")

# 19).Find the lowest annual rainfall using np.min(). 
min_rainfall = np.min(annual_rainfall) 
print(f"Min: {min_rainfall}")

# 20).Find the total annual rainfall using np.sum(). 
sum_rainfall = np.sum(annual_rainfall) 
print(f"Sum: {sum_rainfall}")

# 21).Find the median annual rainfall using np.median(). 
median_rainfall = np.median(annual_rainfall) 
print(f"Median: {median_rainfall}")

# 22).Find the standard deviation using np.std(). 
std_rainfall = np.std(annual_rainfall) 
print(f"Standard Deviation: {std_rainfall}")

# 23).Find the variance using np.var().
var_rainfall = np.var(annual_rainfall) 
print(f"Variance: {var_rainfall}")

# 24).Find the index of the year having the highest rainfall using np.argmax().  
max_index = np.argmax(annual_rainfall)
print("Maximum Rainfall Index:", max_index)

# 25).Find the index of the year having the lowest rainfall using np.argmin(). 
min_index = np.argmin(annual_rainfall)
print("Minimum Rainfall Index:", min_index)

# 26).Sort the annual rainfall values from lowest to highest using np.sort(). 
sort_rainfall = np.sort(annual_rainfall)
print("Sorted Rainfall:", sort_rainfall)

# 27).Create a copy of the annual rainfall array using .copy(), modify the copy, and check the original. 
rainfall_copy = annual_rainfall.copy()

rainfall_copy[0] = 9999
print("Modified Copy:", rainfall_copy[0])
print("Original Array:", annual_rainfall[0])

# 28).Create a slice of the annual rainfall array and modify the slice. Check whether the original array is affected.
rainfall_slice  =  annual_rainfall[0:5]

rainfall_slice[0] = 999
print("Modified Slice:", rainfall_slice)
print("Original Array:", annual_rainfall[:5])

# 29).Randomly select 5 rainfall values from the dataset using np.random.choice().
random_rainfall = np.random.choice(annual_rainfall,size=5,replace=False)
print("Randomly Selected Rainfall:", random_rainfall)
print("Original Rainfall:", annual_rainfall)

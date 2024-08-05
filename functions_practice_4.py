def max_num(a,b,c):
    return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

# ------------------------------------------------

def mult_list(num):
    result = 1
    for i in num:
        result *= i
    return result

numlist = [2, 3, 4]
print(mult_list(numlist))

# ------------------------------------------------

def rev_string(my_str):
    return my_str[::-1]

print(rev_string("cheese"))

# ------------------------------------------------

def num_within(x, low, high):
    return low <= x <= high

x = 5
low = 1
high = 10
print(num_within(x, low, high))

# ------------------------------------------------
# note: solution code, can't figure this one out at ALL.

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)
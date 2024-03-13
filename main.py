from math import floor


def my_sort(data, lo, hi):
  if (lo < hi):
    mid = floor((lo + hi) / 2)
    my_sort(data, lo, mid)
    my_sort(data, mid + 1, hi)
    temp = [0] * (hi - lo + 1)
    l = lo
    r = mid + 1
    temp_index = 0
    while (l <= mid and r <= hi):
      if (data[r] <= data[l]):
        temp[temp_index] = data[r]
        r += 1
        temp_index += 1
      elif (data[l] < data[r]):
        temp[temp_index] = data[l]
        l += 1
        temp_index += 1
    while (r <= hi):
      temp[temp_index] = data[r]
      r += 1
      temp_index += 1
    while (l <= mid):
      temp[temp_index] = data[l]
      l += 1
      temp_index += 1
    k = 0
    while (k < len(temp)):
      data[lo + k] = temp[k]
      k += 1


data = []
print("Enter data to be sorted, finish with -1")
z = float(input())
while (z >= 0):
  data.append(z)
  z = float(input())

lo = 0
hi = (len(data) - 1)

print("unsorted :", data)
my_sort(data, lo, hi)
print("sorted   :", data)

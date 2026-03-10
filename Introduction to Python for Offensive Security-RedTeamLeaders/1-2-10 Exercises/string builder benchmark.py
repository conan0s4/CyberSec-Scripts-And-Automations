'''''''''''
String Builder Benchmark
Compare execution time between concatenating 
10 000 lines with += versus collecting them in a list and "".join. Use time.perf_counter.

'''''''''''

from time import perf_counter


n = 10000
num = []

plus_equals = " "

start1 = perf_counter()
for i in range(n):
    plus_equals += str(i) + " "

end1 = perf_counter()
print(end1 - start1)
print(plus_equals)








s = 10000

numbers = []
plus_equals2 = ""

start2 = perf_counter()
for i in range(s):
    numbers.append(str(i))
plus_equals2 = " ".join(numbers)

end2 = perf_counter()
print(end2 - start2)
print(plus_equals2)





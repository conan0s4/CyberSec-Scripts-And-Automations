'''''''''''
String Builder Benchmark
Compare execution time between concatenating 
10 000 lines with += versus collecting them in a list and "".join. Use time.perf_counter.

note: wrong - solve again
'''''''''''

from time import perf_counter


n = 10000

plus_equals = []

start1 = perf_counter()
for i in range(n):
    plus_equals += [i]

end1 = perf_counter()
print(end1 - start1)





def batch(iterable, n = 1):
   l = len(iterable)
   for ndx in range(0, l, n):
       yield iterable[ndx:min(ndx+n, l)]

for x in batch(range(0, 9), 3):
    print x

print "batch 2" 
arr = [9,7,6,5,4,3,2,1]
for x in batch(arr, 3):
    print x 

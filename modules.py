import math
import statistics
from mymodule import x,y
print(x+y)
from mymodule import b,c
print(b*c)

import mymodule
mymodule.shule("Emobilis Mobile Technology")


# mymodule.num("equal to")
print(mymodule.x * mymodule.y)
print(mymodule.x - mymodule.y)
print(mymodule.x / mymodule.y)
print(mymodule.x + mymodule.y)




##this are inbuild modules
print(math.sqrt(25))
dataset = [6, 2, 14, 78, 4, 7, 1, 87]
x = statistics.mean(dataset)
print("mean is ", x)

a = statistics.mode(dataset)
print("mode is", a)

b = statistics.median_low(dataset)
print("median_low is", b)

c = statistics.median_high(dataset)
print("median_high is ", c)

d = statistics.geometric_mean(dataset)
print("geometric_mean is ", d)

Can you implement a function which can be called like below;

sum(1)(2)(3)(4)... and output must be the sum of all parameters passed.

some examples,
for sum(1)(2)(3)() output must be 6.
for sum(2)(4)(5)(10)() output must be 21.


result = 0
sum(1)
def sum(num)
  result += num
  sum
end

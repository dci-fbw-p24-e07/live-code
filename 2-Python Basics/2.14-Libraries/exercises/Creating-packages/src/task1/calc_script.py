from calculations.addition import sum_operation as a
from calculations.subtraction import minus_operation as s
from calculations.ceiling import ceiling_operation as c
from calculations.powering import power_operation as p

sum_result = a(3, 5)
print("Result of addition is", sum_result)

subtraction_result = s(3, 5)
print("Result of subtraction is", subtraction_result)

ceiling_result = c(3.0 / 9)
print("Result of ceiling is", ceiling_result)

power_result = p(2, 4)
print("Result of powering is", power_result)
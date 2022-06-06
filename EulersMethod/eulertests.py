def assertAlmostEqual(x, y):
    if (abs(x-y) <= 0.01):
        return True
    else:
        raise Exception("Value " + str(x) + " is incorrect.")

from euler import EulersMethod
euler = EulersMethod("y'=x+y/5", 0, -3)
res = euler.execute(x_stop=3, step_size=0.5)

assertAlmostEqual(res["y"], -1.025658)
print("Y-value is correct in the end. (test 1)")
assertAlmostEqual(res["x"], 3.0)
print("X-value is correct in the end. (test 2)")
correctResult = [[0, -3], [0.5, -3.3], [1.0, -3.38], [1.5, -3.218], [2.0, -2.7898], [2.5, -2.0687], [3.0, -1.0256]]
idx = 0
for i in res["values"]:
    assertAlmostEqual(i[0], correctResult[idx][0])
    assertAlmostEqual(i[1], correctResult[idx][1])
    idx += 1
print("All results were equivalent, d.h. correct. (test 3)")
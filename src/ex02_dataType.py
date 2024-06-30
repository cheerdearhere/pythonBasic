
# type check: _class_
x = 100
print(x.__class__) # int
print(x.__class__.__class__) # type
print(type(x))
print(type(type(x)))
# is Instance?
X = 400
print("X isInt? {0}".format(isinstance(X, int)))#True
print("X isFloat? {0}".format(isinstance(X, float)))
print("X isString? {0}".format(isinstance(X, str)))
print("X isBoolean? {0}".format(isinstance(X, bool)))

Y = 400.1
print("Y isInt? {0}".format(isinstance(Y, int)))
print("Y isFloat? {0}".format(isinstance(Y, float)))#True
print("Y isString? {0}".format(isinstance(Y, str)))
print("Y isBoolean? {0}".format(isinstance(Y, bool)))

Z = True
X = 400
print("Z isInt? {0}".format(isinstance(Z, int)))#True
print("Z isFloat? {0}".format(isinstance(Z, float)))
print("Z isString? {0}".format(isinstance(Z, str)))
print("Z isBoolean? {0}".format(isinstance(Z, bool)))#True
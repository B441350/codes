def And(a, b):
    if a == 1 or b == 1 or c == 1:
        return True
    else:
        return False
print(bool( 0 or 0 or 0))
print(bool(0 or 1 or 0))
print(bool(1 or 0 and 1))
print(bool(1 or 1 or 0))
print(bool(0 or 1 or 1))
print(bool(0 or 1 or 0))
print(bool(1 or 1 or 1))
print(bool(1 or 0 or 0))

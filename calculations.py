def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def accuratePerimiter(r):
    #pi = math.pi
    import math
    pi=math.pi
    print(pi)
    return 2 * pi *r

def roughPerimiter(r):
    #perimiter formula 2 x π x radius
    # π= 3.142
    return 2*3.142*r







print(roughPerimiter(3))
print(accuratePerimiter(3))


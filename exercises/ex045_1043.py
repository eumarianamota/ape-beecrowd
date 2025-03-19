def trapezoid(a, b, c):
        trapezoid = ((a + b) * c) / 2
        return f"Area = {trapezoid:.2f}"

def perimeter(a, b, c):
    perimetro = a + b + c
    return f"Perimetro = {perimetro:.1f}"

def isTriangle(a, b, c):
    if (a + b) > c:
        if (a + c) > b:
            if (b + c) > a:
                return perimeter(a, b, c) 
            else:
                return trapezoid(a, b, c)
        else:
            return trapezoid(a, b, c)
    else:
        return trapezoid(a, b, c)


a, b, c = map(float, input().split(" "))
print(isTriangle(a, b, c))


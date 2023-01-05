e= 2.71828                 
def f(x):
    z = eval(fx)            
    return z               

def trapezoidal(a,b,n):
    h = (b - a) / n                  
    integration = f(a) + f(b)       
    for i in range(1,n):            
        k = a + i*h                 
        integration = integration + 2 * f(k)   
    integration = integration * h/2
    return integration            
    
fx = str(input("Masukkan fungsi integral : "))
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
n = int(input("Masukkan jumlah iterasi: "))

result = trapezoidal(a, b, n)
print("Integral dengan metode trapesium: %0.6f" % (result))

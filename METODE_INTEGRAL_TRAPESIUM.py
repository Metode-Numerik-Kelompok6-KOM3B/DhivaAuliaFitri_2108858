#===========Definisikan Fungsi=============#
e= 2.71828                 
def f(x):
    z = eval(fx)                                #eval berfungsi untuk mengoperasikan fungsi dari bentuk string           
    return z                                    #Me return nilai Z

def trapezoidal(a,b,n):
    h = (b - a) / n                                 
    integration = f(a) + f(b)                   #Meintegration fungsi a dan fungsi b      
    for i in range(1,n):            
        k = a + i*h                 
        integration = integration + 2 * f(k)   
    integration = integration * h/2
    return integration            
    
#===========Memasukan Inputan=============#
fx = str(input("Masukkan fungsi integral : "))
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
n = int(input("Masukkan jumlah iterasi: "))

#===========Menampilkan Result=============#
result = trapezoidal(a, b, n)
print("Integral dengan metode trapesium: %0.6f" % (result))

#===========Mendefinisikan Fungsi=============#
e= 2.71828                  
def f(x):
    z = eval(fx)            
    return z             

def simpson13(a,b,n):
    h = (b - a) / n                 
    integration = f(a) + f(b)                   #menjumlahkan fungsi dari batas bawah dan batas bawah
    for i in range(1,n): 
        k = a + i*h                        
        if i%2 == 0:                            #menentukan titik denfan syarat, jika i genap maka f(k) dikali 2
            integration = integration + 2 * f(k)
        elif i%2 == 1:                          #dan jika i ganjil, maka f(k) dikali 4
            integration = integration + 4 * f(k)
    integration = integration * h/3
    return integration                          #Mengembalikan nilai penjumlahan

#===============Masukan Inputan=================#
fx = str(input("Masukkan fungsi integral : "))
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
n = int(input("Masukkan jumlah iterasi: "))

#===============Menampilkan result=================#
result = simpson13(a, b, n)
print("Integral dengan metode trapesium: %0.6f" % (result))

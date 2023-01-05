#=============Definisikan Fungsi===============#
def f1(x):
    return x ** 2 - 20
  
def det_f1(x):
    return 2 * x

 #=============Menerapkan Metode===============#
def newtonRaphson(func, d_func, x, tolerence, max_iterasi, real_root=None):
    if d_func(x) == 0:
        print("Newton Raphson gagal dijalankan.")
        return None                               #Mengembalikan nilai kosong
    else:
        iterasi = 1
        while abs(func(x) / d_func(x)) >= tolerence and iterasi <= max_iterasi:
            iterasi_print = "Iterasi : {0}".format(iterasi)
            if func(x) == 0:
                print(iterasi_print + "Solusi ditemukan : {0}".format(x))
                return x
               
            x = x - func(x) / d_func(x)
            if d_func(x) == 0:
                print("Newton-Raphson gagal dijalankan.")
                return None
            iterasi_print += ", {0}".format(x)
            iterasi = iterasi + 1
            
            print(iterasi_print)
        
        print("\nJumlah iterasi : ",iterasi)
        print("Hasil akhir : ", x)

 #=============Menampilkan hasil==================#        
print(newtonRaphson(f1, det_f1, 1.5, 0.00001, 30, 1))

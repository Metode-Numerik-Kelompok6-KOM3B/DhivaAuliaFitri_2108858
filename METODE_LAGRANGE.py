import numpy as np

#=================Deklarasikan======================#
n = int(input('Masukkan jumlah titik: '))
nilaiX = np.zeros((n))
nilaiY = np.zeros((n))

print('Masukan data X dan Y: ')
for i in range(n):
    nilaiX[i] = float(input( 'nilaiX['+str(i)+']='))
    nilaiY[i] = float(input( 'nilaiY['+str(i)+']='))
    
#===========Mencari titik Interpolasi================#
nilaiXP = float(input('Masukkan titik interpolasi: '))
nilaiYP = 0

#====================Solusi==========================#
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (nilaiXP - nilaiX[j])/(nilaiX[i] - nilaiX[j])
    nilaiYP = nilaiYP + p * nilaiY[i]    
print('Nilai interpolasi untuk titik %.3f adalah %.3f.' % (nilaiXP, nilaiYP))



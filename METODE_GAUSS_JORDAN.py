import numpy as np
import sys

#===============Mendeklarasikan Fungsi=================#
n = int(input('Masukan angka untuk n matriks: '))
matriksA = np.zeros((n,n+1))
matriksHasil = np.zeros(n)

print('Masukan Nilai Koefisien Penjumlahan Matriks:')
for i in range(n):
    for j in range(n+1):
        matriksA[i][j] = float(input( 'matriksA['+str(i)+']['+ str(j)+']='))
for i in range(n):
    if matriksA[i][i] == 0.0:
        sys.exit('Mencari Pembagian dengan 0!')
    for j in range(n):
        if i != j:
            ratio = matriksA[j][i]/matriksA[i][i]
            for k in range(n+1):
                matriksA[j][k] = matriksA[j][k] - ratio * matriksA[i][k]
for i in range(n):
    matriksHasil[i] = matriksA[i][n]/matriksA[i][i]

#=================Menampilkan hasil=====================#
print('\nHasil  : ')
for i in range(n):
    print('X%d = %0.2f' %(i,matriksHasil[i]), end = '\t')

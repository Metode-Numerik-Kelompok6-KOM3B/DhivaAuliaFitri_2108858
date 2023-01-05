def jalanLU(A,b):
  n=len(A)

  #========== matriks L===================#
  L=zeros((n,n))
  for i in range(0,n):
      L[i][i]=1

  #======proses triangularisasi===========#
  for k in range(0,n-1):                  #proses pivot
      if A[k][k]==0:
          for s in range(0,n):
              v=A[k][s]
              u=A[k+1][s]
              A[k][s]=u
              A[k+1][s]=v

      for j in range(k+1,n):
          m=A[j][k]/A[k][k]
          L[j][k]=m                        #nilai m disimpan di matriks L
          for i in range(0,n):
              A[j][i]=A[j][i]-m*A[k][i]
              
  #============print matriks L============#    
  print()
  print('Matriks L')
  print(L)
  #============print matriks U============#  
  print()
  print('Matriks U')
  print(A) 
  
  #======proses subtitusi maju============#
  y=zeros((n,1))
  y[0][0]=b[0][0]/L[0][0]
  for j in range(1,n):
      S=0
      for i in range(0,j):
          S=S+y[i][0]*L[j][i]
      y[j][0]=b[j][0]-S
      
  #======proses subtitusi mundur==========#
  x=zeros((n,1))
  x[n-1][0]=y[n-1][0]/A[n-1][n-1]
  for j in range(n-2,-1,-1):
      S=0
      for i in range(j+1,n):
          S=S+A[j][i]*x[i][0]
      x[j][0]=(y[j][0]-S)/A[j][j]
  print()
  print('Solusinya:\n')
  print("X1 = " + str(x[0]) + "\n")
  print("X2 = " + str(x[1]) + "\n")
  print("X3 = " + str(x[2]) + "\n")
  

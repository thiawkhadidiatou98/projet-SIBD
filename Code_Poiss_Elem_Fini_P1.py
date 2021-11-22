import numpy as np
import matplotlib.pyplot as plt
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Fonction qui construit la matrice de rigidite
def CONST_MAT(N):
    U = 2*np.ones([N])
    V = -np.ones([N-1])
    A = np.diag(U,0) + np.diag(V,1) + np.diag(V,-1)
    return A
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Fonction second membre
def f(x):
    return np.exp(4*x**2)
f = np.vectorize(f) # rendre applicable a des vecteurs la fonction f

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Calcul de la solution
N = 16 
U= np.zeros(N) # Vecteur Solution
x  = np.linspace(0,1,N); # discretisation de [0,1]
F = f(x)  # Vecteur second membre
A = CONST_MAT(N-2) # Matrice Rigidité
Uint = np.linalg.solve(A,F[1:N-1])
U[1:N-1] = Uint
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Affichage de la solution
plt.plot(x, U)



  
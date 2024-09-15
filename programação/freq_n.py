import math

def freq(e,i,l,m,mb):
    return 2/math.pi * math.sqrt((3*e*i)/((l**3)*(m+0.49*mb)))

def inercia(r,d):
    return 2*((math.pi)*(1/4)*(r**4) + (math.pi)*(r**2)*(d**2)) 

def main():

    ### definir os parâmetros da solução ###

    e = 200 * (10**9) #módulo de elasticidade do aço (Pa)
    l = 430 * (10**-3) #comprimento do perfil (eixo z, m)
    m = 10.5 # massa móvel, assumindo chapa de aço de 2mm
    mb =  2.126293 # massa de duas guias lineares de aço, sem contar os fusos
    i = inercia(0.01, 0.036) # d foi extraido do catálogo 

    ### ------------------------------- ###

    print(freq(e,i,l,m,mb))

if __name__ == '__main__': main()


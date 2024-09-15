import math

def freq(e,i,l,m,mb):
    return 2/math.pi * math.sqrt((3*e*i)/((l**3)*(m+0.49*mb)))

def inercia(r,d):
    return 2*((math.pi/4 * r**4) + (math.pi * r**4 * d**2))

def main():

    ### definir os parâmetros da solução ###

    e = 205 * (10**6) #módulo de elasticidade do aço (Pa)
    l = 430 * (10**-3) #comprimento do perfil (eixo z, m)
    m = 7.572936 + 1.384563 # massa móvel, assumindo chapa de aço de 2mm
    mb =  2.126293 # massa de duas guias lineares de aço, sem contar os fusos
    i = inercia(10**-3, 72*10**-3) # d foi extraido do catálogo (devo dividir por dois?) 

    ### ------------------------------- ###

    print(freq(e,l,m,mb,i))

if __name__ == '__main__': main()


import numpy as np

me= 0.511             #9.11e-31 kg electron mass
mp= 938.257           #1.67e-27 kg proton mass
eps=me/mp

wh=1.5          #Hz  proton gyrofrequency
w=0.5           #Hz  wave frequency
x=w/wh
  
wce=3724.0       #Hz electron gyrofrequency
wpe=32449.96     #Hz proton plasma frequency

alfa=(wce**2)/(wpe**2)

n1=0.75         #Hidrogenium fraction
n2=0.20         #Helium fraction
n3=0.05         #Oxygenium fraction

a=1/(1+(eps*x))
b=n1/(x-1)
c=n2/(4*x-1)
d=n3/(16*x-1)

abcd=a+b+c+d
kabcd=abcd/(alfa*eps*x)
uover=1-kabcd
uquad=1/abs(uover)
u=np.sqrt(abs(uquad))

ex=eps**2*x**2

numerador=u*(ex+np.sqrt(ex+((u**2)*(1-ex))))
denominador=ex+(u**2)
vpar=(u*(ex+np.sqrt(ex+((u**2)*(1-ex)))))/(ex+(u**2))
eminimo=((1-(vpar**2))**(-0.5))-1

print('--------------------------')
print('Alfa=',alfa) 
print('U=',uquad)
print('H+: ',n1*100,'%')
print('He+: ',n2*100,'%')
print('O+: ',n3*100,'%')
print('Wavefrequency: ',w,' Hz')
print('E_min = ',eminimo,' MeV')
print('--------------------------')



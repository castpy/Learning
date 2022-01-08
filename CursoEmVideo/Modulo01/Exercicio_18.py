import math
ang = float(input('Digite um angulo qualquer: '))
print('O angulo {} tem o SENO {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O angulo {} tem o COSSENO {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O angulo {} tem a TANGENTE {:.2f}'.format(ang, math.tan(math.radians(ang))))
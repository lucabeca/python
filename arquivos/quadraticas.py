def verificar(num):
    if not str(num).isalpha():
        return num
    else:
        print("Foi inserido um dígito inválido.")
        exit()

def verificar_funcao(a):
    if a == 0:
        print("O 'a' não pode ser igual a zero.")
        exit()
    else:
        return a

print('Calculadora de funções quadráticas')
print('by Lucas')

#inserindo variáveis#

a = float(input('\nA: '))
verificar(a)
verificar_funcao(a)
b = float(input('B: '))
verificar(b)
c = float(input('C: '))
verificar(c)

#calculando delta#

delta = (b ** 2) -4 * a * c
r_delta = delta ** 0.5
m_delta = delta * -1

print('\nDelta:', delta)

#calculando baskhara#

m_b = b * -1
d_a = 2 * a

if delta < 0:
    print('Não há raiz para delta negativo.')
elif delta == 0:
    x1 = round((m_b + r_delta) / d_a, 2)
    x2 = round((m_b - r_delta) / d_a, 2)
    print('x:', x1,)
else:
    x1 = round((m_b + r_delta) / d_a, 2)
    x2 = round((m_b - r_delta) / d_a, 2)
    print('x¹:', x1,'\nx²:', x2)


#calculando vértices#

vy = round(m_delta / (4 * a), 2)
vx = round(m_b / (2 * a), 2)

print('Vértice y:', vy)
print('Vértice x:', vx)

if delta < 0:
    if b == 0:
        print("\n({}, {})".format(vx, vy))
    else:
        print("\n({}, {})".format(vx, vy))
elif delta == 0:
    if b == 0:
        print("\n({}, {}))".format(vx, vy))
else:
    print("\n({}, {}) | ({}, 0) | ({}, 0)".format(vx, vy, x1, x2))

#verificando sinal da função#

if delta < 0:
    print("f(x)>0 -> x>",vy)
    print("f(x)<0 -> x<",vy)
elif delta == 0:
    print('f(x)=0 -> x = {}'.format(x1,))
else:
    print('\nf(x)>0 -> {}< x <{}'.format(x1, x2))
    print('f(x)<0 -> {}< x <{}'.format(x2, x1))
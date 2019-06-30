def verificar(num):
    if a == 0:
        print("O 'a' não pode ser igual a zero.")
        exit()
    if not str(num).isalpha():
        return num
    else:
        print("Foi inserido um dígito inválido.")
        exit()

print('Calculadora de funções quadráticas')
print('by Lucas')

a = float(input('\nA: '))
verificar(a)
b = float(input('B: '))
verificar(b)
c = float(input('C: '))
verificar(c)

delta = (b ** 2) - (4 * a * c)
r_delta = delta ** 0.5
m_delta = delta * -1
m_b = b * -1
d_a = 2 * a
vy = round(m_delta / (4 * a), 2)
vx = round(m_b / (2 * a), 2)

print('\nDelta:', delta)
print('Vértice y:', vy)
print('Vértice x:', vx)

if delta < 0:
    print('Não há raiz para delta negativo')
    if a > 0:
        print("\nA função será sempre positiva")
    if a < 0:
        print("\nA função será sempre negativa")
elif delta == 0:
    x = round((m_b + r_delta) / d_a, 2)
    print('x:', x)
    print("\n({}, {}))".format(vx, vy))
    print('f(x)>0 -> {}< x <{}'.format(vx, vx))
    print('f(x)<0 -> {}< x <{}'.format(vx, vx))
    print('f(x)=0 -> x = {}'.format(x))
else:
    x1 = round((m_b + r_delta) / d_a, 2)
    x2 = round((m_b - r_delta) / d_a, 2)
    print('x¹:', x1,'\nx²:', x2)
    print('\nf(x)>0 -> {}< x <{}'.format(x1, x2))
    print('f(x)<0 -> {}< x <{}'.format(x2, x1))
    print('f(x)=0 -> x = {}, {}'.format(x1, x2))
    print("\n({}, {}) | ({}, 0) | ({}, 0)".format(vx, vy, x1, x2))

print("\nObrigado por usar :)")

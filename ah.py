ahorro = 30000000
saldo = 0
cuota = 5000
dia = 1

while saldo < ahorro:
    valor = (dia*cuota)
    saldo = valor +saldo
    print('dia',dia,' cuota $',valor,' ahorro $',saldo)
    dia = dia + 1
    ahorro = ahorro - saldo

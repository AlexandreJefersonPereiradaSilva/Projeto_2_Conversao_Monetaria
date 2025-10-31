valor_dolar:8.75

with open('vendas_dolar.txt','r')as entrada,open('vendas_real.txt','w')as saida:
    for linha in entrada:
        linha = linha.strip()
        if linha:
            valor_real = float(linha) * valor_dolar
            saida.write("f{valor_real:.2f}\n")

print("Operação Realizada com sucesso! Salvo em vendas_real")
    
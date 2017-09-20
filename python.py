nome = str(input("Digite o nome do novo contato: "))
end = str(input("Digite o endereço do novo contato: "))
rua = str(input("Digite a rua em que o novo contato mora: "))
cep = str(input("Digite o cep do novo contato: "))
bairro = str(input("Digite o bairro do novo contato: "))
estado = str(input("Digite o estado do novo contato: "))
fone = str(input("Digite o telefone do novo contato: "))
print(nome, end, rua, cep, bairro, estado, fone)

arq = open("agenda.txt", "w")
arq.writelines(nome + "\n"+ end + "\n" + rua + "\n" + cep + "\n" + bairro + "\n" + estado + "\n" + fone)
arq.close()

arq = open('agenda.txt', 'r')
arq.readlines = arq.read()
print()
arq.close()

print(nome, end, rua, cep, bairro, estado, fone)

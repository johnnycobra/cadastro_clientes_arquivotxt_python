
#abrindo o arquivo
arquivo = open("D:\_uteis\cadastro_clientes.txt", "w")

#loop do cadastro de clientes
while True:
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    estado = input("Digite o estado do cliente: ")

    #gravando os dados no arquivo txt
    arquivo.write("Nome: " + nome + "\n")
    arquivo.write("Email: " + email + "\n")
    arquivo.write("Cidade: " + cidade + "\n")
    arquivo.write("Estado: " + estado + "\n\n")

    #pergunta
    resposta = input("Deseja cadastrar outro cliente? (s/n) ")
    if resposta == "n":
        break


arquivo.close()
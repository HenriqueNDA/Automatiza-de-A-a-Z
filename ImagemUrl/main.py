from simple_image_download import simple_image_download as simp
import os.path
import os


imagens = simp.simple_image_download
converted_list = []
final = open('Resultado.csv', 'w')
link = []

file = input("Nome do arquivo: ")
nimagens = int(input("Deseja salvar quantas imagens relacionada ao produto? "))
cls = lambda: os.system('cls')
final.write('Descrições' + ';' 'Link')

if os.path.isfile(file):
    descricoes = open(file, 'r')
    cls()
    print("Iniciando....")
    for element in descricoes:
        converted_list.append(element.strip())

    for linha in converted_list:
        for nlink in range(nimagens):
            print('\nNome: ' + linha)
            link = imagens().urls(linha, nimagens)
            final.write('\n' + linha + ';' + link[nlink])

    descricoes.close()
    cls()
    print('\nProcesso finalizado!!')
    print('Arquivo Resultado.csv salvo dentro da pasta!!')
    os.system("pause")
else:
    cls()
    print("\nArquivo informado não encontrado...")
    print('Processo finalizado!!')
    os.system("pause")



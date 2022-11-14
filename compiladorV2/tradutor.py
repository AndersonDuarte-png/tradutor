from mimetypes import init
import os

#objeto organizar a fila dos objt
class estado:
    def __init__(self, p_anterior, valor, p_proximo):
        self.p_anterior = p_anterior
        self.valor = valor
        self.p_proximo = p_proximo

class estado_especial:
    def __init__(self, p_anterior, p_anterior2, valor, p_proximo,p_proximo2):
        self.p_anterior = p_anterior2
        self.p_anterior2 = p_anterior
        self.valor = valor
        self.p_proximo= p_proximo
        self.p_proximo2 = p_proximo2

#variaveis globais
global x 
x = 1
global x_aux 
x_aux = 0



def separar_token(valor):
    array = valor.split(" ")
    return array

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def leitor(caminho):
    vet_arquivo = []
    with open(f""+caminho) as file:
        for i in file:
           vet_arquivo.append(str.strip(i))
    return vet_arquivo

#achar onde corre a decisão
def num_rep(vet_num):
    sucesso = None
    cont = 0
    for a in vet_num:
        for i in vet_num:
            if i == a:
                cont +=1
                if cont == 2:
                    sucesso= a
        cont = 0
    indices = [i for i, item in enumerate(vet_num) if item == sucesso]

    return indices


def reorganizar_numeros(id,vet_num_esq,vet_num_dir,vet_numeros,vet_linha_new_oredem_numeros):
    if id == 1:
        last_direita =""
        vet_caminho = []

        indices_numero_repetido = num_rep(vet_num_esq)

        for i in range(0,len(vet_num_esq)):

            if i == indices_numero_repetido[0]:
                break
            vet_linha_new_oredem_numeros.append(str(f"{vet_num_esq[i]} {vet_num_dir[i]}"))


        for i in indices_numero_repetido:
            vet_linha_new_oredem_numeros.append(str(f"{vet_num_esq[i]} {vet_num_dir[i]}"))
            last_direita = vet_num_dir[i]
            
            for a in range(i+1,len(vet_num_esq)):
                if vet_num_esq[a] == last_direita:
                    vet_linha_new_oredem_numeros.append(str(f"{vet_num_esq[a]} {vet_num_dir[a]}"))
                    last_direita = vet_num_dir[a]

        '''
        for i in indices_numero_repetido:
            print(i)
        for i in vet_linha_new_oredem_numeros:
            print(i)
        '''


def situacao_concorrencia(vet_linha,vet_place):
    vet_place = None
    vet_new_ordem = []
    p = 0
    p2 = p+1
    salvar =""
    for i in vet_linha:
        vet_temp = separar_token(str(i))
        linha = []
        for a in vet_temp:
            if not (isnumber(a)) :
                linha.append(a)
        if len(linha) > 3:
            if linha.index('|') == 1:
                print(f'p{p} {linha[0]}')
                print(f'{linha[0]} p{p+1}')
                print(f'{linha[0]} p{p2 +1}')
                p+=1
                p2 = p+1
                print(f'p{p} {linha[2]}')
                print(f'p{p2} {linha[3]}')
                print(f'{linha[2]} p{p+2} ')
                print(f'{linha[3]} p{p2+2} ')
                p+=2
                p2 = p+1
            else:
                print(f'{salvar} p{p}')
                print(f'{salvar} p{p2}')
                print(f'p{p} {linha[0]}')
                print(f'p{p2} {linha[1]}')
                p=p2
                p2 = p+1
                print(f'{linha[0]} p{p+1}')
                print(f'{linha[1]} p{p2+1}')
                print(f'p{p + 1} {linha[3]}')
                print(f'p{p2 + 1} {linha[3]}')
                p+=1
                p2 = p+1
        else:
            print(f'p{p} {linha[0]}')
            print(f'p{p2} {linha[0]}')
            print(f'{linha[0]} p{p2+1}')
            print(f'p{p2 + 1} {linha[2]}')
            p = p2 + 2
            p2 = p+1
        last = len(linha) -1
        salvar = linha[last]
        last_total = len(vet_linha) -1
        if i in vet_linha[last_total]:
            print(f'{salvar} p0')








def situacao_padrao(vet_numeros, vet_valores,vet_place):
    global x
    global x_aux

    a = len(vet_numeros)
    a = a-1
    final = int(len(vet_valores))
    final -= 1
    cont = 0

    for i in vet_valores:

        novo_estado = estado(str(f"p{x_aux}"),str.strip(i),str(f"p{x}"))
        vet_place.append(novo_estado)  
        
        x_aux = x
        x = x + 1

        cont += 1
        if  final == cont and vet_numeros[a] == '0':
            x = 0

def situacao_decisao(vet_numeros, vet_linha,vet_place):
    #vet_new_linha = []
    vet_linha_new_oredem_numeros = []
    vet_new_ord_valores = []
    vet_num_esq = []
    vet_num_dir = []
    #vet_new_ord_numeros = []

    vet_num_esq.append(int(vet_numeros.pop(0)))
    vet_num_dir.append(int(vet_numeros.pop(1)))
    cont = 2

    for i in vet_numeros:
        if cont % 2 == 0 or cont == 0:
            vet_num_esq.append(int(i))
        else:
            vet_num_dir.append(int(i))
        cont+=1

    reorganizar_numeros(1,vet_num_esq,vet_num_dir,vet_numeros,vet_linha_new_oredem_numeros)

    for numeros in vet_linha_new_oredem_numeros:
        for linha in vet_linha:
            if str(numeros) in str(linha):
                
                #print(f"sucesso em {numeros} in {linha}")

                linha_tratada = separar_token(linha)
                for i in linha_tratada:
                    if not (isnumber(i) or i == '|'):
                        vet_new_ord_valores.append(i)
    
    '''
    #vetor com os numeros
    for i in range(0, len(vet_linha_new_oredem_numeros)):
        numeros_ao_meio = separar_token(str(vet_linha_new_oredem_numeros[i]))
        vet_new_ord_numeros.append(numeros_ao_meio[0])
        vet_new_ord_numeros.append(numeros_ao_meio[1])
    '''

    cont = 0
    cont_aux = 0
    salvar_depois = None
    salvar_valor = None
    validador = 0

    for valores in vet_new_ord_valores:
        antes = cont
        #print(f"cont: {cont} e vet: {vet_new_ord_valores[cont]}")

        if (cont + 1) == len(vet_new_ord_valores):
            depois = 0
        else:
            depois = cont+1

        if "[" in vet_new_ord_valores[depois] and salvar_valor == None:
            salvar_valor = str.strip(valores)
            salvar_depois = depois
        elif "[" in vet_new_ord_valores[cont] and salvar_valor != None and validador != 0:
            novo_estado = estado(str(f"p{antes}"), str.strip(salvar_valor), str(f"p{salvar_depois}"))
            vet_place.append(novo_estado)
            antes = salvar_depois

        novo_estado = estado(str(f"p{antes}"),str.strip(valores),str(f"p{depois}"))
        vet_place.append(novo_estado)

        if "[" in str.strip(valores):
            validador +=1

        cont +=1


#valida qual o tipo da entrada
def validar_numeros(vet_linha,numeros):
    
    for i in vet_linha:
        vet_temp = separar_token(str(i))
        linha = []
        for a in vet_temp:
            if not (isnumber(a)):
                linha.append(a)
        if len(linha) > 3:
            return 2

    for atual in numeros:
        cont = 0
        for atual_lista in numeros:
            if atual == atual_lista:
                cont+=1
        if cont > 2:
            return 1
        else:
            cont = 0
    return 0


#organiza as places separandos valores, numeros, cacteres(|) e organizando o proximo e anterior
def organizar_places(vet_linha, vet_place):

    numeros = []
    valores = []
    valor = None

    for l in vet_linha:
        linha_tratada = separar_token(l)

        for i in linha_tratada:
            if isnumber(i) == True:
                numeros.append(i)

            if not (isnumber(i) or i == '|'):
                valores.append(i)


    tipo = validar_numeros(vet_linha,numeros)


    if tipo == 0:
        print("situação tipo padrão")
        situacao_padrao(numeros,valores,vet_place)
        valor =0
    elif tipo == 1:
        print("situação tipo descisao")
        situacao_decisao(numeros,vet_linha,vet_place)
        valor = 1
    elif tipo == 2:
        print("situação tipo concorrencia")
        situacao_concorrencia(vet_linha,vet_place)
        valor = 2
    return valor

        
#escrevendo o resultado final
def conversor_in(arquivo):
    vet_input = [".inputs"]
    vet_outputs = [".outputs"]
    vet_place = []
    vet_linha = []
    with open("resultado.txt","a") as file:
        for i in arquivo:
            if "Input" in i:
                token = separar_token(i)
                resultado = token[1] 
                vet_input.append(resultado)
                
            elif "Output" in i:
                token = separar_token(i)
                resultado = token[1] 
                vet_outputs.append(resultado)
            
            else:
                vet_linha.append(str(i))

        for i in vet_input:
            file.write(f"{i}")
            l = len(vet_input) -1
            if i == vet_input[l]:
                file.write("\n")
            elif i == 's':
                file.write(f", ")
            else:
                file.write(f", ")

        for i in vet_outputs:
            file.write(f"{i}")
            l = len(vet_outputs) -1
            if i == vet_outputs[l]:
                file.write("\n.graph\n")
            elif i == 's':
                file.write(f", ")
            else:
                file.write(f", ")
        tipo = organizar_places(vet_linha, vet_place)

        if not (vet_place == None):
            for i in vet_place:
                file.write(str(f".{i.p_anterior} {i.valor}\n"))
                file.write(str(f".{i.valor} {i.p_proximo}\n"))

        file.write('.marking{p0}\n.end')
    if tipo == 1:
        arrumar_arquivo()

def arrumar_arquivo():
    linhas = []
    repetidos = ""
    with open("resultado_new.txt","a") as new_file:
        with open("resultado.txt") as file:
            for i in file:
                linhas.append(str.strip(i))

        for i in range(0,len(linhas)-1):
            for a in range(i+1,len(linhas)-1):
                if linhas[i] in linhas[a]:
                    repetidos = int(a)

        linhas.pop(repetidos)
        for i in linhas:
            new_file.write(str.strip(i))
            new_file.write('\n')
    os.remove('resultado.txt')
    os.rename('resultado_new.txt', 'resultado.txt')

def orquestrador():
    arquivo = leitor(input("caminho do arquivo: "))
    conversor_in(arquivo)


if __name__ == '__main__':
    orquestrador()
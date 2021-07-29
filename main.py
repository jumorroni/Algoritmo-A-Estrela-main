from distancias import Distancia
from arvore import Arvore
from estado import No
from cidades import Cidades

def a_estrela(Arvore, base_distancias, inicio, fim, distancia_inicial):

    lista_abertos = []
    lista_fechados = []

    no_inicial = No(nome = inicio, h = distancia_inicial)
    no_final = No(nome = fim)

    lista_abertos.append(no_inicial)

    while len(lista_abertos) > 0:
        print(f'lista abertos: {lista_abertos}\n')

        # organizar a lista em ordem crescente de funcao e pegar o menor
        lista_abertos.sort()
        no_atual = lista_abertos.pop(0)

        # inserir no atual na lista_fechados
        lista_fechados.append(no_atual)
        print(f'lista fechados: {lista_fechados}\n')

        # verificar se chegou no destino
        if no_atual == no_final:
            caminho = []
            while no_atual != no_inicial:
                caminho.append(no_atual.nome + ': ' + str(no_atual.g))
                no_atual = no_atual.pai
            caminho.append(no_inicial.nome + ': ' + str(no_inicial.g))
            return caminho[::-1]

        # verificar vizinhos
        vizinhos = Arvore.get(no_atual.nome)
        print(f'nos vizinhos: {vizinhos}\n')

        # Loop entre vizinhos
        for chave in vizinhos.keys():
            vizinho = No(chave, no_atual)
            if(vizinho in lista_fechados):
                continue
            # calculo do custo acumulado e funcao
            vizinho.g = no_atual.g + Arvore.get(no_atual.nome, vizinho.nome)
            vizinho.h = base_distancias.get(vizinho.nome)
            vizinho.f = vizinho.g + vizinho.h if vizinho.h is not None else vizinho.g
            if(inserir_lista_abertos(lista_abertos, vizinho) == True):
                lista_abertos.append(vizinho)

    # caminho nao encontrado
    return None


# verificar se vizinho deve ser incluido em lista_abertos
def inserir_lista_abertos(lista_abertos, vizinho):
    for aberto in lista_abertos:
        # f do vizinho precisa ser menor
        if (vizinho == aberto and vizinho.f > aberto.f):
            return False
    return True



def main():
    distancia_padrao = Distancia()
    arvore = Arvore()

    lista_cidades = (Cidades()).lista_cidades
    cidades = (Cidades()).cidades_string

    # interacao com user
    opcao_origem = input(f'{cidades}Insira o código da cidade origem: ')
    opcao_origem = lista_cidades[int(opcao_origem) - 1]
    opcao_destino = input(f'{cidades}Insira o código da cidade destino: ')
    opcao_destino = lista_cidades[int(opcao_destino) - 1]
    origem = opcao_origem
    destino = opcao_destino

    # pegando distancias ja configuradas pra montar lista personalizada
    lista_destino = {}
    for item in distancia_padrao.distancias_dict:
        lista_destino[item] = distancia_padrao.distancias_dict[item][destino][0]

    # "criar" grafo de conexoes entre cidades
    arvore.ligar('Sao_Joao_da_Baliza', 'Sao_Luiz', distancia_padrao.distancias_dict['Sao_Joao_da_Baliza']['Sao_Luiz'][1] )
    arvore.ligar('Sao_Joao_da_Baliza', 'Rorainopolis', distancia_padrao.distancias_dict['Sao_Joao_da_Baliza']['Rorainopolis'][1] )
    arvore.ligar('Sao_Joao_da_Baliza', 'Caroebe', distancia_padrao.distancias_dict['Sao_Joao_da_Baliza']['Caroebe'][1] )
    arvore.ligar('Sao_Luiz', 'Sao_Joao_da_Baliza', distancia_padrao.distancias_dict['Sao_Luiz']['Sao_Joao_da_Baliza'][1] )
    arvore.ligar('Sao_Luiz', 'Canta', distancia_padrao.distancias_dict['Sao_Luiz']['Canta'][1] )
    arvore.ligar('Sao_Luiz', 'Caracarai', distancia_padrao.distancias_dict['Sao_Luiz']['Caracarai'][1] )
    arvore.ligar('Rorainopolis', 'Caracarai', distancia_padrao.distancias_dict['Rorainopolis']['Caracarai'][1] )
    arvore.ligar('Rorainopolis', 'Sao_Luiz', distancia_padrao.distancias_dict['Rorainopolis']['Sao_Luiz'][1] )
    arvore.ligar('Rorainopolis', 'Canta', distancia_padrao.distancias_dict['Rorainopolis']['Canta'][1] )
    arvore.ligar('Caracarai', 'Iracema', distancia_padrao.distancias_dict['Caracarai']['Iracema'][1] )
    arvore.ligar('Caracarai', 'Sao_Luiz', distancia_padrao.distancias_dict['Caracarai']['Sao_Luiz'][1] )
    arvore.ligar('Iracema', 'Caracarai', distancia_padrao.distancias_dict['Iracema']['Caracarai'][1] )
    arvore.ligar('Iracema', 'Mucajai', distancia_padrao.distancias_dict['Iracema']['Mucajai'][1] )
    arvore.ligar('Iracema', 'Alto_Alegre', distancia_padrao.distancias_dict['Iracema']['Alto_Alegre'][1] )
    arvore.ligar('Mucajai', 'Iracema', distancia_padrao.distancias_dict['Mucajai']['Iracema'][1] )
    arvore.ligar('Mucajai', 'Boa_Vista', distancia_padrao.distancias_dict['Mucajai']['Boa_Vista'][1] )
    arvore.ligar('Alto_Alegre', 'Iracema', distancia_padrao.distancias_dict['Alto_Alegre']['Iracema'][1] )
    arvore.ligar('Alto_Alegre', 'Amajari', distancia_padrao.distancias_dict['Alto_Alegre']['Amajari'][1] )
    arvore.ligar('Alto_Alegre', 'Boa_Vista', distancia_padrao.distancias_dict['Alto_Alegre']['Boa_Vista'][1] )
    arvore.ligar('Amajari', 'Alto_Alegre', distancia_padrao.distancias_dict['Amajari']['Alto_Alegre'][1] )
    arvore.ligar('Amajari', 'Pacaraima', distancia_padrao.distancias_dict['Amajari']['Pacaraima'][1] )
    arvore.ligar('Amajari', 'Boa_Vista', distancia_padrao.distancias_dict['Amajari']['Boa_Vista'][1] )
    arvore.ligar('Pacaraima', 'Uiramuta', distancia_padrao.distancias_dict['Pacaraima']['Uiramuta'][1] )
    arvore.ligar('Pacaraima', 'Normandia', distancia_padrao.distancias_dict['Pacaraima']['Normandia'][1] )
    arvore.ligar('Pacaraima', 'Amajari', distancia_padrao.distancias_dict['Pacaraima']['Amajari'][1] )
    arvore.ligar('Pacaraima', 'Boa_Vista', distancia_padrao.distancias_dict['Pacaraima']['Boa_Vista'][1] )
    arvore.ligar('Normandia', 'Uiramuta', distancia_padrao.distancias_dict['Normandia']['Uiramuta'][1] )
    arvore.ligar('Normandia', 'Bonfim', distancia_padrao.distancias_dict['Normandia']['Bonfim'][1] )
    arvore.ligar('Normandia', 'Pacaraima', distancia_padrao.distancias_dict['Normandia']['Pacaraima'][1] )
    arvore.ligar('Normandia', 'Boa_Vista', distancia_padrao.distancias_dict['Normandia']['Boa_Vista'][1] )
    arvore.ligar('Bonfim', 'Normandia', distancia_padrao.distancias_dict['Bonfim']['Normandia'][1] )
    arvore.ligar('Bonfim', 'Boa_Vista', distancia_padrao.distancias_dict['Bonfim']['Boa_Vista'][1] )
    arvore.ligar('Canta', 'Boa_Vista', distancia_padrao.distancias_dict['Canta']['Boa_Vista'][1] )
    arvore.ligar('Canta', 'Rorainopolis', distancia_padrao.distancias_dict['Canta']['Rorainopolis'][1] )
    arvore.ligar('Canta', 'Sao_Luiz', distancia_padrao.distancias_dict['Canta']['Sao_Luiz'][1] )
    arvore.ligar('Uiramuta', 'Pacaraima', distancia_padrao.distancias_dict['Uiramuta']['Pacaraima'][1] )
    arvore.ligar('Uiramuta', 'Normandia', distancia_padrao.distancias_dict['Uiramuta']['Normandia'][1] )
    arvore.ligar('Uiramuta', 'Boa_Vista', distancia_padrao.distancias_dict['Uiramuta']['Boa_Vista'][1] )

    # tornan arvore nao dirigida, criar ligacoes simetricas
    arvore.nao_dirigida()
    caminho = a_estrela(arvore, lista_destino, origem, destino, distancia_padrao.distancias_dict[origem][destino][0])
    print(caminho)

if __name__ == "__main__": main()
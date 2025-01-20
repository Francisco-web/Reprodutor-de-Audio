import pygame
import sys
import os

# Inicializa o mixer do pygame
pygame.mixer.init()

musica_carregada = False

def carregar_musica(caminho):
    global musica_carregada
    try:
        pygame.mixer.music.load(caminho)
        musica_carregada = True
        print(f"Música '{caminho}' carregada com sucesso!")
    except pygame.error as e:
        musica_carregada = False
        print(f"Erro ao carregar a música: {e}")

def reproduzir_musica():
    if musica_carregada == True:
        pygame.mixer.music.play()
        print("Reproduzindo música...")
    else:
        print("Nehuma música foi carregada! Por favor, Carrega uma nova música.")

def pausar_musica():
    pygame.mixer.music.pause()
    print("Música pausada.")

def retomar_musica():
    pygame.mixer.music.unpause()
    print("Música retomada.")

def parar_musica():
    pygame.mixer.music.stop()
    print("Música parada.")

def ajustar_volume(volume):
    pygame.mixer.music.set_volume(volume)
    print(f"Volume ajustado para {volume * 100}%")

def menu():
    print("\nComandos do Reprodutor:")
    print("1. Carregar música (forneça o caminho)")
    print("2. Reproduzir música")
    print("3. Pausar música")
    print("4. Retomar música")
    print("5. Parar música")
    print("6. Ajustar volume (0.0 a 1.0)")
    print("7. Sair")

def obter_caminho_musica_padrao():
    # A variavel pasta_musica guarda o caminho para a pasta de músicas padrão do pc
    pasta_musicas = os.path.join(os.path.expanduser('~'), 'Music')
    return pasta_musicas

def main():
    while True:
        menu()
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            caminho_padrao = obter_caminho_musica_padrao()
            print(f"Caminho padrão de músicas: {caminho_padrao}")
            arquivo = input("Insira o nome do arquivo MP3: ")
            caminho_completo = os.path.join(caminho_padrao, arquivo)
            carregar_musica(caminho_completo)
        elif escolha == '2':
            reproduzir_musica()
        elif escolha == '3':
            pausar_musica()
        elif escolha == '4':
            retomar_musica()
        elif escolha == '5':
            parar_musica()
        elif escolha == '6':
            volume = float(input("Defina o volume (0.0 a 1.0): "))
            ajustar_volume(volume)
        elif escolha == '7':
            print("Encerrando o reprodutor...")
            pygame.mixer.quit()
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
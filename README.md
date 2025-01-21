# Reprodutor-de-áudio
Reprodutor de áudio é um projecto criado como resposta a um desafio proposto durante a formação de aprendizagem da linguagem de programação Python.
Projecto simples de reprodução de arquivos de aúdio, o desafio é o exercício número 021 proposto pelo professor Gustavo Guanabara em seu curso Python Mundo 1 - da aula 08 usando módulos. Muito interessante!

O objectivo do programa é a criação de funções básicas para carregar, reproduzir, pausar, parar e ajustar o volume do áudio.
Para a manipulação de áudio com python, usei a biblioteca pygame que oferece funcionalidades através do módulo pygame.mixer.music. O pygame é uma biblioteca robusta para desenvolvimento de jogos e multimídia em python. E uma das suas fucionalidade é reprodução, mixagem e controle sobre volume, canais de áudio e suporte para diferentes tipos de arquivos de áudio (mp3, mpeg, etc). Por isso escolhi para usar neste projecto. 

Principais Funcionalidades:
1. Inicialização do Mixer de Áudio:
   - Antes de usar qualquer funcionalidade de áudio, é necessário inicializar o mixer.
   pygame.mixer.init()

2. Carregar Música:
   - Carrega um arquivo de música (MP3, OGG, etc.) para reprodução.
   pygame.mixer.music.load('caminho/para/seu_arquivo.mp3')

3. Reproduzir Música:
   - Inicia a reprodução do arquivo de música carregado. 

4. Parar a Reprodução:
   - Para a música imediatamente.
   pygame.mixer.music.stop()
  
5. Pausar e Retomar Música:
   - Pausa a música atual e permite retomá-la de onde parou.
   pygame.mixer.music.pause()
   pygame.mixer.music.unpause()

6. Configurar Volume:
   - Define o volume da música, onde 1.0 é o volume máximo e 0.0 é mudo.
   pygame.mixer.music.set_volume(0.5)  # Volume em 50%
   

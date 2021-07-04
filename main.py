from pytube import YouTube, Playlist

print("#" * 40)
print("Seja bem vindo")
print("desenvolvido por Leonardo Appio")
print("#" * 40)


def baixar_video(url_video):
    yt = YouTube(url_video)
    yt.streams.get_highest_resolution().download()


while True:
    print("[1] - Baixar um vídeo na sua melhor resolução")
    print("[2] - Baixar uma playlist inteira de vídeos")
    print("[3] - Baixar apenas o áudio de um vídeo")

    numero_escolha = (input("Digite o número da sua escolha: "))

    if numero_escolha == '1':

        url_video = input("Insira a URL do Vídeo que deseja baixar: ")
        print('baixando...')
        baixar_video(url_video)
        print("Seu video foi baixado com sucesso, acesse ele na pasta onde se encontra este executável")

    elif numero_escolha == '2':

        url_playlist = input("Insira a URL da Playlist que deseja baixar: ")
        playlist = Playlist(url_playlist)
        nome_playlist = input("Digite um nome para a pasta onde será salva a sua playlist: ")

        print("Os seguintes vídeos estão sendo baixados: ")

        for index, video in enumerate(playlist):
            print("[", index + 1, "] - ", video)
            videobaixado = YouTube(video)
            stream = videobaixado.streams.get_highest_resolution()
            stream.download(output_path=nome_playlist)

        print("Todos os vídeos foram baixados!")

    elif numero_escolha == '3':
        url_audio = input('Insira a URL do vídeo que você deseja baixar o áudio: ')
        yt = YouTube(url_audio)
        audio = yt.streams.filter(only_audio=True)[0]
        print('baixando...')
        audio.download()
        print('Seu áudio foi baixado!')
    else:
        print("Escolha inválida [digite um número de 1-3]")

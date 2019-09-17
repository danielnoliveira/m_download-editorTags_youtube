import os,json,requests,eyed3

def recognize(musica):
    f = open('./'+musica,'rb')
    data = {
        'return': 'timecode,apple_music,deezer,spotify',
        'api_token':'your_api_token'
    }
    result = requests.post('https://api.audd.io/', data=data,files=dict({'file':f}))
    # print(result.text)
    # with open('teste.json','w') as f:
        # json.dump(json.loads(result.text),f,indent=4)
    # with open('teste.json') as f:
    #     data = json.load(f)
    data = json.loads(result.text)
    audiofile = eyed3.load('./'+musica)
    if 'result' in data.keys() and data['result']!=None:
        audiofile.tag.artist = data['result']['artist']
        if 'deezer' in data['result'].keys():
            album = data['result']['deezer']['album']['title']
        else:
            album = data['result']['album']
        audiofile.tag.album = album
        audiofile.tag.album_artist = album
        audiofile.tag.title = data['result']['title']
        print(data['result']['title'],' done')
        audiofile.tag.save()
        os.rename('./'+musica,'../'+data['result']['title'].replace('/','')+'.mp3')
    else:
        # print('data['error']')
        print(musica+' fail')
if __name__ == "__main__":
    print('Bem vindo(a) à MusicDEapp(D="Download",E="Editor")')
    print('Informações básicas:')
    print('1. O programa pode baixar uma musica ou uma playlist(completa ou em pedaços)')
    print('2. Basta fornecer a url do video ou da playlist')
    print('3. Após baixar a(s) musica(s) o script irá atualizar os metadados da musica:')
    print('    -Album,Title e Artist ')
    print('4. Todas as musicas baixadas serão colocadas na pasta cob')
    print('5. Após serem editadas serão movidas para a pasta musics')
    while(True):
        print('Opções:')
        print('1.Baixar musica de um video')
        print('2.Baixar musicas de uma playlist')
        print('3.Corrigir musicas no diretorio')
        print('4.Encerrar script')
        op = int(input('Opção desejada:'))
        if op == 1:
            url = input('Link do video:')
            os.system('./ytd.sh '+url)
            musicas = os.listdir('./')
            for m in musicas:
                if m.endswith('.mp3'):
                    recognize(m)
        elif op == 2:
            url = input('Link da playlist:')
            itens = list(map(str,input('Itends da playlist(num1 num2 num3 ...)').split()))
            os.system('./ytd-2.sh '+url+' '+','.join(itens))
            musicas = os.listdir('./')
            for m in musicas:
                if m.endswith('.mp3'):
                    recognize(m)
        elif op == 3:
            musicas = os.listdir('./')
            for m in musicas:
                if m.endswith('.mp3'):
                    recognize(m)
        else:
            print('Script encerrando...')
            print('Script encerrado!!')
            exit(0)
    

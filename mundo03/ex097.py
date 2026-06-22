def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


escreva('Ricardo Cezar')
escreva('Fez mais um exercício de Python')
escreva('Done!')
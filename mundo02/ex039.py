from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
anos_pessoa = ano_atual - ano

print(f'Quem nasceu em {ano} tem \033[31m{anos_pessoa}\033[m anos em {ano_atual}.')

if anos_pessoa < 18:
    faltam_anos = 18 - anos_pessoa
    alista_futuro = ano_atual + faltam_anos
    if faltam_anos == 1:
        print(f'Ainda falta {faltam_anos} ano para o alistamento.')
    else:
        print(f'Ainda faltam {faltam_anos} anos para o alistamento.')
    print(f'Seu alistamento será em {alista_futuro}.')
elif anos_pessoa > 18:
    passam_anos = anos_pessoa - 18
    alista_passado = ano_atual - passam_anos
    if passam_anos == 1:
        print(f'Você já deveria ter se alistado há {passam_anos} ano.')
    else:
        print(f'Você já deveria ter se alistado há {passam_anos} anos.')
    print(f'Seu alistamento foi em {alista_passado}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
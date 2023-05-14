from countryinfo import CountryInfo

print('=-' * 30)
print('\033[032mProgramado por JulianoMarthins\033[m')
print('=-' * 30)
print()

def info():
    print()
    print(f'País: {pais.name()}')
    print(f'Capital: {pais.capital()}')
    print(f'Moeda: {pais.currencies()}')
    print(f'Idiomas: {pais.languages()}')
    print(f'País que fazem fronteira: {pais.borders()}')
    print(f'Códico de área: {pais.calling_codes()}')
    print(f'População: {pais.population()}')
    print(f'Tamanho territórial: {pais.area()}')
    print(f'Estados: {pais.provinces()}')
    print(f'Continente: {pais.region()}')
    print()


while True:
    try:
        pais = CountryInfo(input('Digite o nome do país: '))
    except:
        print('\033[031mERRO!!!   Você digitou um valor inválido\033[m')

    info()

    print('\n', '=-' * 30)
    cond = str(input('\nDeseja continuar? [S/N] ')).lower()

    if 's' in cond:
        print()
        print('=-' * 30)
        continue
    elif 'n' in cond:
        break


print('\n', '=-' * 30)
print('Obrigado por usar')





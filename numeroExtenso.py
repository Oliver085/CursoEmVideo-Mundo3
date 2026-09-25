numero=int(input('Digite um número entre 0 e 20: '))
if numero <= 20:
   numeroExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
   print(f'Voce digitou o número {numero} que por extenso é {numeroExtenso[numero]}')
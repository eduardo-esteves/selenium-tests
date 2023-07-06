# O assert sempre verifica se o retorno da condição é True.
assert True

num_esperado = 1
num_obtido = 1

assert num_obtido == num_esperado, f'Esperado {num_obtido} mas obtido {num_esperado}'

text_1 = 'Selenium'
text_2 = 'Selenium Webdriver'

assert text_1 in text_2, f'Texto {text_1} não faz parte de {text_2}'




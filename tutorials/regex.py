import re

txt = "Пожалуйста, отправляйте свои заявки на адрес электронной почты inbox@example.com или по телефону 123456."

reg_exps = [r' ', r'\S+', r'\w+|\S', r'\w+|\S+',r'\w+', r'((?:\w+@\w+\.\w+)|\w+|\S)', r'((?:\w+@\w+\.\w+)|\S|\w+)']


correct = ['Пожалуйста', ',', 'отправляйте', 'свои', 'заявки', 'на', 'адрес', 'электронной', 'почты', 'inbox@example.com', 'или', 'по', 'телефону', '123456', '.']
for reg_exp in reg_exps:
    tokenize_regex = re.compile(reg_exp, re.I)
    tokens = tokenize_regex.findall(txt)

    print(reg_exp)
    print("Result:", tokens)
    print("OK:", tokens == correct)
    print()
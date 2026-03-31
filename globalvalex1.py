def learn_ai():
    Sub1='Ai'#Here Sub1 is called local
    print('To implement {} Based application we use {} language'.format(Sub1,Lang))
def learn_ml():
    Sub2='Ml'#Sub2 is called local variable
    print('To implement {} Based application we use {} language'.format(Sub2,Lang))
print('Main program')
Lang='Python'#Lang is called global variable
learn_ai()
learn_ml()

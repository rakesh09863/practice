a='python'
for val in a:
    print(val)
print('-'*50)
for val in a:
    if val in ['t','o']:
        continue
    print(val)

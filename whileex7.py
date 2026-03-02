#program for accepting a word / Line and display each and every letter
line=input('enter the value:')
i=0
while(i<len(line)):
    print(line[i])
    i=i+1
print('-'*50)
i=-1
while(i>-len(line)):
    print(line[i])
    i=i-1
print('-'*50)
i=len(line)-1
while(i>0):
    print(line[i])
    i=i-1
print('-'*50)
i=-len(line)
while(i<-1):
    print(line[i])
    i=i+1
print('-'*50)
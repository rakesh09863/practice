while(True):
    a=input('enter the value:')
    if len(a)==0:
        print('don`t enter space try again')
    elif  not a.isdigit():
        print('enter only +ve numbers try again')
    else:
        a=int(a)
        if a>0:
            break
    print('invalid input try again--')
while(True):
    words=input('enter the name of a student:').strip()
    if len(words)==0:
        print('don`t enter the space')
    else:
        res='valid'
        for word in words.split():
            if not word.isalpha():
                res='invalid'
                break
        if res=='invalid':
            print('{} is invalid try again-- '.format(words))
        else:
            break
while(True):
    cm=input('enter the cm marks:').strip()
    if len(cm)==0:
        print('don`t enter the space try again')
    elif not cm.isdigit():
        print('don`t enter the alphabets')
    else:
        cm=int(cm)
        if 0<=cm<=100:
            break
        else:
            print('{} invalid try again'.format(cm))
while(True):
    cppm=input('enter the cppm marks:').strip()
    if len(cppm)==0:
        print('don`t enter the space try again')
    elif not cppm.isdigit():
        print('don`t enter the alphabets')
    else:
        cppm=int(cppm)
        if 0<= cppm<=100:
            break
        else:
            print('{} invalid try again'.format(cppm))
while(True):
    osm=input('enter the osm marks:').strip()
    if len(osm)==0:
        print('don`t enter the space try again')
    elif not osm.isdigit():
        print('don`t enter the alphabets')
    else:
        osm=int(osm)
        if 0<=osm<=100:
            break
        else:
            print('{} invalid try again'.format(osm))
total=cm+cppm+osm
percentage=round((total/300)*100,2)
if cm < 40 or cppm < 40 or osm < 40:
    grade='fail'
else:
    if 250<=total<=300:
        grade='distinction'
    elif 200<= total<=249:
        grade='first'
    elif 150<=total<=199:
        grade='second'
    elif 120<=total<=149:
        grade='third'
    else:
        grade='fail'
print('\troll number={}'.format(a))
print('\tname of a student={}'.format(words))
print('\tmarks of cm={}'.format(cm))
print('\tmarks of cppm={}'.format(cppm))
print('\tmarks of osm={}'.format(osm))
print('\ttotal marks={}'.format(total))
print('\tpercentage={}'.format(percentage))
print('\tgrade={}'.format(grade))
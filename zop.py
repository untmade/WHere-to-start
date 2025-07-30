print('This will ask for your zip')
zip=''
while zip=='':
    print('Enter your zip')
    zip=str(input())
    if len(zip)!=5 or not zip.isdigit():
        zip=''
        print('Do not be a bitch!')
    else:
        print('your zip code is',zip, 'and it has been saved')

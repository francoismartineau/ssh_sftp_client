import util_sftp as sftp
import util_ssh as ssh
import util


while True:
    util.clear_console()
    print('\n\n\n\t[1] Upload file')
    print('\t[2] Download file')
    print('\t[3] Navigate')
    choix = input('\t')
    if choix == '1':
        sftp.upload_file(input('\n\tfile path: '))        
        input()
    elif choix == '2':
        pass
    elif choix == '3':
        pass

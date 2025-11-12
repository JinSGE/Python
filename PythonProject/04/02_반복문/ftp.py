def help():
    help_msg = """
    Commands may be abbreviated.  Commands are:

    !		    debug		mdir	sendport	site
    $		    dir		    mget	put		    size
    account		disconnect	mkdir	pwd		    status
    append		exit		mls		quit		struct
    """
    print(help_msg)
def ls():
    ls_msg = """
    ls        	list contents of remote directory
    """
    print(ls_msg)

while True:
    cmd = input('ftp> ')
    if cmd == 'quit':
        break
    elif cmd == 'help':
        help()
    elif cmd == 'ls':
        ls()
    else:
        print('?Invalid command')

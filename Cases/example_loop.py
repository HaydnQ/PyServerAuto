from Librarys.SimpleSSH import *


def main(loop=None):
    host.loop(loop=loop)
    host.run("/ls", 'pwd', "cd /home", "pwd")
    

if __name__ == '__main__':
    Loops = 5
    host = host_set_up()
    if Loops == 1:
        main()
    else:
        for current_loop in range(1, Loops+1):
            main(current_loop)
    host.close_connection()

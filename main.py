
#import log_reader
from wo_maker import Wo

#input files
logfilefuse  = r'in\wo\rfs.txt'

w = Wo(logfilefuse)
def main():

    #w.get_appname()
    w.owner()
    #w.signon()
    #w.get_protocol()
    #w.get_group()
    w.close()

if __name__ == "__main__":
    main()
    
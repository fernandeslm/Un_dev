
#import log_reader
from wo_maker import Wo

#input files
logfilefuse  = r'in\wo\RFS-1-12099724937.txt'

w = Wo(logfilefuse)
def main():

    w.get_appname()
    w.get_owner()
    w.signon()
    w.get_protocol()
    w.get_group()

if __name__ == "__main__":
    main()
    
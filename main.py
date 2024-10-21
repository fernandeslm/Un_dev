
#import log_reader
from wo_maker import Wo

#input files
logfilefuse  = r'in\wo\rfs.txt'

w = Wo(logfilefuse)
def main():

    w.close()

if __name__ == "__main__":
    main()
    

#import log_reader
import wo_maker

#input files
logfilefuse  = r'in\wo\RFS-1-11915182725.txt'

def main():

    comment = wo_maker.get_app(logfilefuse)
    print(comment)
    
if __name__ == "__main__":
    main()
    
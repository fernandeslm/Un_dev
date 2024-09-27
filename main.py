
#import log_reader
import wo_maker

#input files
logfilefuse  = r'in\wo\RFS-1-12003843920.txt'

def main():

    comment = wo_maker.get_app(logfilefuse)
    print(comment)
    wo_maker.get_owner(logfilefuse)
    wo_maker.signon(logfilefuse)
    wo_maker.get_protocol(logfilefuse)
    comment = wo_maker.get_group(logfilefuse)
    print(comment)

if __name__ == "__main__":
    main()
    
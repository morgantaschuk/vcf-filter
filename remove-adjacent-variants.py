#!/bin/python

from __future__ import print_function
import sys,getopt,fileinput

def usage():
    print('Removes variants that overlap with each other\n')
    print("remove-adjacent-variants.py <file>")
    print(" use -v to print discarded variants to stderr")
    print(" use -h to print this message")


def main(argv):
    vcffile=None
    verbose=False


    if "-h" in argv:
       usage()
       sys.exit(2)
    if "-v" in argv:
       verbose=True
       argv=argv.remove('-v')
    vcf=fileinput.input()


    pstart=0
    pend=0

    for line in vcf:
        line=line.strip()

        if line.startswith("#"):
            print(line)
        else:
            linebits=line.split()
            nstart=int(linebits[1])
            
            #find the maximum length of the variant at this position
            alts=linebits[4].split(",")
            maxalt=0
            for a in alts:
               lalt=len(a)
               if lalt>maxalt:
                   maxalt=lalt
            nend=nstart+maxalt

            #end of the previous alt is within or after start of this variant, ignore (send to stderr)
            if pend >= nstart:
                if verbose:
                    print("#Pstart",pstart,"pend",pend,"nstart", nstart, "nend", nend, file=sys.stderr)    
                    print(line, file=sys.stderr)
                pass
            #next alt is after end of previous alt, print to stdout and set new baseline
            else:
                print(line)
                pstart=nstart
                pend=nend
                       

if __name__ == "__main__":
    main(sys.argv)



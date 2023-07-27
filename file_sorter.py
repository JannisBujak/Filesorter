# import modules used here -- sys is a very standard one
import sys, argparse, logging, os
import shutil
from tqdm import tqdm

def copy_file(filename, Pathname, new_foldername):    
    joinPathname = os.path.join(Pathname, new_foldername)    
    if not os.path.exists(joinPathname):
        print()
        print(f"Creating dir %s" % joinPathname)
        os.makedirs(joinPathname, exist_ok=True)
        
    filesrc = os.path.join(Pathname, filename)
    filedst = os.path.join(joinPathname, filename)

    #print(f"From %s to %s" % (filesrc, filedst))
    if not os.path.exists(filedst):
        shutil.copyfile(filesrc, filedst)
        


def restructure(Pathname, Ciphers):
    
    files = os.listdir(Pathname)
    logname = "filesorter.log"
    
    log = open(os.path.join(Pathname, logname), "w")    
    Prefixes = set()
    
    for i in tqdm(range(len(files))):
        file = files[i]        
        if not os.path.isfile(os.path.join(Pathname, file)) or (file == logname): 
            continue
        
        iUnderscore = file.find('_')       

        if iUnderscore < 0:
            log.write(f"! %s\n" % file)
            continue
            
        Prefix = file[:iUnderscore+1]
        if not Prefix in Prefixes:
            log.write(f"%s\n" % Prefix)
            log.flush()
            Prefixes.add(Prefix)
        
        new_foldername = file[len(Prefix):len(Prefix)+Ciphers]
        copy_file(file, Pathname, new_foldername)
        
  
if __name__ == '__main__':
    print()
    parser = argparse.ArgumentParser( 
                                    description = "Does a thing to some stuff.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
    parser.add_argument(
                      "Pathname",
                      help = "Path of the folder the files are in",
                      metavar = "Pathname",
                      default='.')

    parser.add_argument(
                      "--Ciphers",
                      help = "Ciphers of the series of letters used for the later folders",
                      metavar = "Ciphers",  
                      default=4,
                      type=int)
    args = parser.parse_args()
    
    restructure(args.Pathname, args.Ciphers)
    
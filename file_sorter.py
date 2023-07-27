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
    shutil.copyfile(filesrc, filedst)
        

def restructure(Pathname, Prefix, Ciphers):
    
    files = os.listdir(Pathname)
    
    for i in tqdm(range(len(files))):
        file = files[i]
        
        if not os.path.isfile(os.path.join(Pathname, file)): 
            continue
         
        if not file.startswith(Prefix):
            print()
            print(f"File %s does not match Pattern (\"%s\")" % (file, Prefix))
            continue
            
        new_foldername = file[len(Prefix):len(Prefix)+Ciphers]
        copy_file(file, Pathname, new_foldername)
  
if __name__ == '__main__':
    print()
    parser = argparse.ArgumentParser( 
                                    description = "Does a thing to some stuff.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
    parser.add_argument(
                      "--Pathname",
                      help = "Path of the folder the files are in",
                      metavar = "Pathname",
                      default='.')
    parser.add_argument(
                      "--Prefix",
                      help = "Prefix of the Name-Pattern",
                      metavar = "Prefix",                      
                      required=True)
    parser.add_argument(
                      "--Ciphers",
                      help = "Ciphers of the series of letters used for the later folders",
                      metavar = "Ciphers",  
                      default=4,
                      type=int)
    args = parser.parse_args()
    print(args)
    
    restructure(args.Pathname, args.Prefix, args.Ciphers)
    
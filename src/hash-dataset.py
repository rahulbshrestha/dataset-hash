import os, sys, hashlib, time
import mmh3
from hashlist import Hashlist
from collections import Counter

# Generate hash for all files in a directory 
def hash_directory(dirname):
    hashlist = []

    for root, dirs, files in os.walk(dirname, followlinks=False):
        for file in files:
            hashlist.append((file, murmur_hash_file(os.path.join(root, file))))

    return hashlist

# Generate MD5 hash for a file
def md5_hash_file(filename):
    hash = hashlib.md5()
    # TODO: consider when file is too large and can't be fit in memory
    with open (filename, 'rb') as f:
        content = f.read()
        hash.update(content)
    return hash.hexdigest()

def murmur_hash_file(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    hash = mmh3.hash_bytes(data, 0xBEFFE)
    return hash.hex()

def sum_hashes(list):
    sum = 0
    for item in list:
        sum = sum + int(float(item[1]))
    return sum

# Calculate similarity % between two lists
def check_similarity(list1, list2):

    #Converting lists to tuples for comparision
    #c1 = Counter(map(tuple, list1))
    #c2 = Counter (map(tuple,list2))
    
    c1 = Counter(list1)
    c2 = Counter(list2)

    diff = c1 - c2
    #TODO: Consider c2 - c1 case also 

    common = c1 & c2
    
    c1_length = float(sum(c1.values()))
    c2_length = float(sum(c2.values()))
    diff_length = float(sum(diff.values()))
    common_length = float(sum(common.values()))
    
    if (opt_nomatch):
        print('Non-matching samples: \n', list(diff))

    if (opt_match):
        print('Matching samples: \n', list(common))

    similarity_score = ((common_length / max(c1_length, c2_length))* 100) 
    return similarity_score



# Usage instructions
def usage():
    print ("Usage: python3 src/dataset-hash.py [OPTIONS] [FILES]")
    print ("-n        -  Display samples that don't match.")
    print ("-m        -  Displays samples that are matching.")
    print ("-p        -  Print hash lists of both datasets.  ")
    
# Produce a Windows-style filename
def winfname(filename):
    return filename.replace("/","\\")

# Normalize filename based on platform
def normfname(filename):
    if os.name == 'nt': #for Windows
        return filename.replace("/", "\\")
    else:
        return filename.replace("\\","/")


if __name__ == '__main__':
    
    start_time = time.time()
    opt_nomatch = None
    opt_match = None
    opt_print = None

    if len(sys.argv) == 1:
        usage()
        sys.exit(0)

    # Resolve command line options
    args = sys.argv[1:]
    it = iter(args)
    for i in it:
        if i == '-n':
            opt_nomatch = True
            continue
        elif i == '-m':
            opt_match = True
            continue
        elif i == '-p':
            opt_print = True

    h1 = Hashlist()
    h2 = Hashlist()

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]

    # Hash every file inside a directory and put it in a list 
    h1.hashlist = hash_directory(dir1)
    h2.hashlist = hash_directory(dir2)

    h1.shuffle()
    h2.shuffle()
    
    h1.pop(1000)
    h2.pop(1000)

    # Print list of hashes
    if (opt_print):
        h1.print()
        h2.print()

    #Calculate similarity between two lists 
    print("Similarity %: ", check_similarity(h1.hashlist, h2.hashlist))

    print("Execution time: %s seconds" % (time.time() - start_time))



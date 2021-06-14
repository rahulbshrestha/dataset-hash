import os, sys, hashlib, time
from collections import Counter

# Generate hash for all files in a directory 
def hash_directory(dirname):
    hashlist = []

    for root, dirs, files in os.walk(dirname, followlinks=False):
        for file in files:
            hashlist.append((file, hash_file(os.path.join(root, file))))

    return hashlist

# Generate MD5 hash for a file
def hash_file(filename):
    hash = hashlib.md5()
    
    with open (filename, 'rb') as f:
        content = f.read()
        hash.update(content)
    return hash.hexdigest()

# Print contents of a list
def print_list(list):
    for item in list:
        print (item)
    print('\n')

# Calculate similarity % between two lists
# def check_similarity(list1, list2):
#     score = len(set(list1) & set(list2)) / float(len(set(list1) | set(list2))) * 100
#     return score

#Calculate similarity % between two lists
def check_similarity(list1, list2):
    c1 = Counter(list1)
    c2 = Counter (list2)
    diff = c1 - c2
    common = c1 & c2
    
    c1_length = float(sum(c1.values()))
    c2_length = float(sum(c2.values()))
    diff_length = float(sum(diff.values()))
    
    if (opt_nomatch):
        print('Non-matching samples: \n', list(diff))

    if (opt_match):
        print('Matching samples: \n', list(common))

    similarity_score = 100 - ((diff_length / max(c1_length, c2_length))* 100) 
    return similarity_score


# Usage instructions
def usage():
    print ("Usage: python3 dataset-hash.py [OPTIONS] [FILES]")
    print ("-n        -  Display samples that don't match")
    print ("-n        -  Displays samples that are matching")
    
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

    if len(sys.argv) == 1:
        usage()
        sys.exit(0)

    args = sys.argv[1:]

    it = iter(args)
    for i in it:
        if i == '-n':
            opt_nomatch = True
            continue
        elif i == '-m':
            opt_match = True
            continue

    hashlist1 = []
    hashlist2 = []

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
 
    hashlist1 = hash_directory(dir1)
    hashlist2 = hash_directory(dir2)

    print_list(hashlist1)
    print_list(hashlist2)

    #Calculate similarity between two lists 
    print("\nSimilarity %: ", check_similarity(hashlist1, hashlist2))

    print("\nExecution time: %s seconds" % (time.time() - start_time))
        


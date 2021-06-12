import os, sys, hashlib, time, glob

#Generate MD5 hash of file
def md5hash(filename):
    hash = hashlib.md5()
    
    with open (filename, 'rb') as f:
        content = f.read()
        hash.update(content)
    return hash.hexdigest()

# Calculate similarity % between two lists
def similarity_score(list1, list2):
    score = len(set(list1) & set(list2)) / float(len(set(list1) | set(list2))) * 100
    return score

def usage():
    print ("Usage: dataset-hash.py [OPTIONS] [FILES]")
    
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

    if len(sys.argv) == 1:
        usage()
        sys.exit(0)

    args = sys.argv[1:]

    hashlist1 = []
    hashlist2 = []
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    

    for filename in glob.iglob(dir1 + '**/**', recursive=True):
        if (os.path.isfile(filename)):
            hashlist1.append((md5hash(filename)))
    
    for filename in glob.iglob(dir2 + '**/**', recursive=True):
        if (os.path.isfile(filename)):
            hashlist2.append((md5hash(filename)))

    # print('Hashlist1: \n')
    # for hash in hashlist:
    #     print ('%s  %s\n'%(hash[1], hash[0]))
    
    # print('Hashlist2: \n')
    # for hash in hashlist2:
    #     print ('%s  %s\n'%(hash[1], hash[0]))

    #Calculate similarity between two lists 
    #print("Similarity %: ", similarity_score(hashlist1, hashlist2))

    print("\nExecution time: %s seconds" % (time.time() - start_time))
        


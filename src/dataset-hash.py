import os, sys, hashlib

def md5hash(filename, directory):
    hash = hashlib.md5()
    filename = directory + filename

    with open (filename, 'rb') as f:
        content = f.read()
        hash.update(content)
    return hash.hexdigest()

# def md5sum(filename, blocksize):
#     hash = hashlib.md5()
#     with open(filename, "rb") as f:
    #         for block in iter(lambda: f.read(blocksize), ""):
    #             hash.update(block)
#     return hash.hexdigest()

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
        
    if len(sys.argv) == 1:
        usage()
        sys.exit(0)

    args = sys.argv[1:]

    hashlist = []
    hashlist2 = []
    main_dir = sys.argv[1]
    main_dir2 = sys.argv[2]
    
    for filename in os.listdir(main_dir):
        hashlist.append((filename, md5hash(filename, main_dir)))

    for filename2 in os.listdir(main_dir2):
        hashlist2.append((filename2, md5hash(filename2, main_dir2)))
        
    #for hash in hashlist:
    #    print ('%s  %s\n'%(hash[1], winfname(hash[0])))

    # Calculate similarity between two lists
    similarity_score = len(set(hashlist) & set(hashlist2)) / float(len(set(hashlist) | set(hashlist2))) * 100  
    print("Similarity %: ", similarity_score)
        


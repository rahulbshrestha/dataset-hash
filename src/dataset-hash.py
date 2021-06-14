import os, sys, hashlib, time

# Generate hash of all files in a directory recursively
def hash_directory(dirname):
    hashlist = []

    for root, dirs, files in os.walk(dirname):
        for file in files:
            hashlist.append((hash_file(os.path.join(root, file))))

    return hashlist

# Generate MD5 hash of file
def hash_file(filename):
    hash = hashlib.md5()
    
    with open (filename, 'rb') as f:
        content = f.read()
        hash.update(content)
    return hash.hexdigest()

# Print contents of list
def print_list(list):
    for item in list:
        print (item)
    print('\n')

# Calculate similarity % between two lists
def check_similarity(list1, list2):
    score = len(set(list1) & set(list2)) / float(len(set(list1) | set(list2))) * 100
    return score

# Usage instructions
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
 
    hashlist1 = hash_directory(dir1)
    hashlist2 = hash_directory(dir2)

    print_list(hashlist1)
    print_list(hashlist2)

    #Calculate similarity between two lists 
    print("Similarity %: ", check_similarity(hashlist1, hashlist2))

    print("\nExecution time: %s seconds" % (time.time() - start_time))
        


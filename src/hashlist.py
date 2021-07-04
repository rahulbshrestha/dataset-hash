import csv
import random

class Hashlist:

    def __init__(self):
        self.hashlist = []

    # Print contents of list
    def print(self):
        for item in self.hashlist:
            print (item)
        print('\n')
    
    
    # Save list into csv file
    def save(self, filename):
        save_dir = "output/" + filename
        with open(save_dir, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.hashlist)

    # Load contents of csv file into a list
    def load(self, filename):
        load_dir = "output/" + filename
        with open(load_dir, newline='') as f:
            reader = csv.reader(f)
            self.hashlist = list(reader)

    # Randomly change order of elements in list
    def shuffle(self):
        random.shuffle(self.hashlist)

    def sort(self):
        self.hashlist.sort()

    def pop(self, n):
        del self.hashlist[:n]
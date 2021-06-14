# dataset-hash
Implementing a hashing technique to compare large scale, out of core machine learning datasets

### Instructions

To compare two datasets: 

```
python3 src/dataset-hash.py data/small-dataset-1 data/small-dataset-2
```

Available options: 

```
python3 src/dataset-hash.py [OPTIONS] [FILES]

-m : Dispaly samples that are matching
-n : Display samples that don't match
```
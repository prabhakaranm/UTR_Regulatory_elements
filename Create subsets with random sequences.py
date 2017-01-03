from sys import argv
import random

with open(argv[1]) as f:
    file = f.read()

seq_ind = file.split(">")
seq_ind.pop(0)

number_of_sequences = [i for i in range(len(seq_ind))]

subset_total = 500 # number of subsets to create

for i in range(subset_total):
    filename = "subset_%s.fas" % i
    rand_sample = random.sample(number_of_sequences, 10) # take 10 random numbers without replacement
    output = open(filename, "w")
    for j in rand_sample:
        seq = ">" + seq_ind[j]
        output.write(seq)
    output.close()
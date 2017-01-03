from Bio import SeqIO
 
input_seq_iterator = SeqIO.parse(open("input_filename.fas", "rU"), "fasta")
long_seq_iterator = (record for record in input_seq_iterator \
                      if len(record.seq) > 10)
 
output_handle = open("output_filename.fasta", "w")
SeqIO.write(long_seq_iterator, output_handle, "fasta")
output_handle.close()
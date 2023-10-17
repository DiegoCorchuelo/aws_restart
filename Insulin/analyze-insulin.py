with open('preproinsulin-seq.txt', 'r') as file:
    preproinsulin_seq = file.read()

preproinsulin_seq = preproinsulin_seq.replace('ORIGIN', '').replace('61', '').replace('1', '').replace('//', '').replace(' ', '').replace('\n', '')

with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(preproinsulin_seq)


lsinsulin_seq_clean = preproinsulin_seq[:24]
binsulin_seq_clean = preproinsulin_seq[24:54]
cinsulin_seq_clean = preproinsulin_seq[54:89]
ainsulin_seq_clean = preproinsulin_seq[89:]


with open('lsInsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin_seq_clean)

with open('bInsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin_seq_clean)

with open('cInsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin_seq_clean)

with open('aInsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin_seq_clean)
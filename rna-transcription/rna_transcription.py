def to_rna(dna_strand):
    dna_strand = dna_strand.upper()
    rna_strand = []
    replace = {'G':'C','C':'G','T':'A','A':'U'}
    for letter in dna_strand:
        if letter in replace:
            rna_strand.append(replace[letter])
        else:
            raise ValueError("Invalid Input: Data needs to contain G,C,T or A")
    rna = ''.join(rna_strand)
    return rna

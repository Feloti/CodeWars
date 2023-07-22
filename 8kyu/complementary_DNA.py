def DNA_strand(dna):
    dna_list = list(dna)
    for i in range(len(dna)):
        if(dna_list[i]) == "T":
            dna_list[i] = "A"
        elif(dna_list[i]) == "A":
            dna_list[i] = "T"
        elif(dna_list[i]) == "C":
            dna_list[i] = "G"
        else:
            dna_list[i] = "C"
    return ''.join(dna_list)

print(DNA_strand("ATCG"))
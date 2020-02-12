# Introduction to Programming, Task 25,Lists,Functions, and String Handling
# Ndou Pfarelo Rudolph 2019/11/03
# Creating my function to translate DNA code

# opening the DNA text file in read and write mode
with open("DNA.txt", "r+") as dna_file:
    DNA = dna_file.read().replace("\n", "")
    dna_count = len(DNA)

    # creating the dictionary using single-letter data-base codes and DNA codons for the translate function
    amino_acids_dict = {"ATT":"I",
                    "ATC":"I",
                    "ATA":"I",
                    "CTT":"L","CTC":"L","CTA":"L","CTG":"L","TTA":"L", "TTG":"L",
                    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
                    "TTT":"F","TTC":"F",
                    "ATG":"M",}

# creating a function to translate DNA text file into  single-letter data-base
def translate(DNA):
    # defining the variable
    trans_dna = ""
    for i in range(0,dna_count,3):
        codon = DNA[i:i+3]
        keys = amino_acids_dict.keys()
        if codon in amino_acids_dict:
            trans_dna +=  amino_acids_dict[codon]
        else:
            trans_dna += 'X'
    return trans_dna
# printing the result of the translated DNA text file  
print(translate(DNA))

# defining the variable
MDNA = ""
# creating the a function the indentify first character "a"
def mutate (MDNA):
    # opening normalDNA and mutatedDNA text file 
    with open("DNA.txt", "r") as rf, open("normalDNA.txt", "w") as wf, open("mutatedDNA.txt", "w") as pf:
        
                # using for loop to copy DNA text file to normalDNA and mutatedDNA text file
                for line in rf:
                    # using write function replace character a in the normalDNA and mutatedDNA text file
                    singleLine = line.replace("\n","")
                    wf.write(singleLine.replace("a","A"))
                    pf.write(singleLine.replace("a","T"))
                    
# return function
mutate(MDNA)

# defining the variable
normalDNA = ""
mutatedDNA = ""
# creating txtTranslate function to translate normalDNA and mutatedDNA
def txtTranslate(normalDNA,mutatedDNA):
    # opening normalDNA and mutatedDNA text file in read mode
    with open("normalDNA.txt", "r+") as rf, open("mutatedDNA.txt", "r+") as pf:
        # reading the text file
        normalDNA = rf.read()
        mutatedDNA = pf.read()
    # printing the translated normalDNA and mutatedDNA file
    print (translate(normalDNA)),print (translate(mutatedDNA))
# calling the txtTranslate function
txtTranslate(normalDNA,mutatedDNA)


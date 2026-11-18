# My Day 24 Python Mini Project
# Name: Maham Fayyaz
# Project: DNA Base Counter & Sequence Analyzer
# What I practiced today: Nested Functions & Function Workflow
# (Nested Functions, Inner & Outer Functions, Return Values,
# Function-to-Function Data Flow, String Methods, DNA Base Counting,
# and Function Workflow)

def get_dna():
    return " ATGCGTAA "
dna = get_dna()
print(dna)

def clean_dna(dna):
    return dna.strip()
cleaned_dna = clean_dna(dna)
print(cleaned_dna)    

def process_dna(cleaned_dna):
    def get_length():
        return len(cleaned_dna)
    return get_length()
length = process_dna(cleaned_dna)
print(length)       

def count_bases(cleaned_dna):
    a_count = cleaned_dna.count("A")
    t_count = cleaned_dna.count("T")
    g_count = cleaned_dna.count("G")
    c_count = cleaned_dna.count("C") 
    return a_count, t_count, g_count, c_count
result = count_bases(cleaned_dna)
print(result)    
print("______Final Result Of This Program______")
def show_result(dna_sequence,dna_length,a,t,g,c):
    print("\nDNA Sequence:", dna_sequence)
    print("DNA Length:", dna_length)
    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)
show_result("ATGCGTAA",length, 3, 2, 2, 1)    
print("_____________***Completed***_____________")

# Today's mini project is complete.
# I practiced Nested Functions using DNA Length Calculation,
# Function Workflow using DNA Processing,
# and String Methods for DNA Base Counting.
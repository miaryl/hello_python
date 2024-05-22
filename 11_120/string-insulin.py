# Store the human preproinsulin sequence in a variable called preproinsulin:
prepro_insulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

print(prepro_insulin)

# Store the remaining sequence elements of human insulin in variables:
ls_insulin = "malwmrllpllallalwgpdpaaa"
b_insulin = "fvnqhlcgshlvealylvcgergffytpkt"
a_insulin = "giveqcctsicslyqlenycn"
c_insulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# merge b_insulin and a_insulin and store insulin

insulin = b_insulin + a_insulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")

print(prepro_insulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + a_insulin)

# calculating the molecular weight of insulin
# creating a list of the amino acid (AA) weights
aa_weights = {
    'A' : 89.09,
    'C' : 121.16,
    'D' : 133.10,
    'E' : 147.13,
    'F' : 165.19,
    'G' : 75.07,
    'H': 155.16, 
    'I': 131.17,
    'K': 146.19, 
    'L': 131.17,
    'M': 149.21,
    'N': 132.12,
    'P': 115.13, 
    'Q': 146.15, 
    'R': 174.20, 
    'S': 105.09, 
    'T': 119.12,
    'V': 117.15, 
    'W': 204.23, 
    'Y': 181.19
}

# count the number of each amino acids
aa_count_insulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Multiply the count by the weights
molecular_weight_insulin = sum({x: (aa_count_insulin[x]*aa_weights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())

print("The rough molecular weight of insulin: " +
str(molecular_weight_insulin))

molecular_weight_insulin_actual = 5807.63
print("Error percentage: " + str(((molecular_weight_insulin - molecular_weight_insulin_actual)/molecular_weight_insulin_actual)*100))
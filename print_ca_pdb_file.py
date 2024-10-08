def filter_c_alpha(input_pdb, output_pdb):
    with open(input_pdb, 'r') as infile, open(output_pdb, 'w') as outfile:
        for line in infile:
            if line.startswith("ATOM") and " CA " in line:
                outfile.write(line)

# Usage
input_pdb_file = 'step5_input2.pdb'  
output_pdb_file = '1_file.pdb'  

filter_c_alpha(input_pdb_file, output_pdb_file)


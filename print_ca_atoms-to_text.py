def extract_atom_indices(pdb_file, output_file):
    with open(pdb_file, 'r') as pdb, open(output_file, 'w') as out:
        atom_indices = []
        for line in pdb:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom_index = line[6:11].strip()  # Atom index is in columns 7-11
                atom_indices.append(atom_index)
        
        out.write(','.join(atom_indices))

pdb_file = 'example.pdb'
output_file = 'atom_indices.txt'
extract_atom_indices(pdb_file, output_file)

print(f"Atom indices have been written to {output_file}")


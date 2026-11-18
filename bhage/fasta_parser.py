def parse_fasta(file):

    records = []
    current_id = None
    sequence_lines = []
    valid_nucleotides = set("ACGTRYSWKMBDHVN")
    

    for temp in file:
        # Check for Header
        if temp.startswith(">"):

            # Check for new Header
            if current_id is not None:
                # Save previous header / DNA
                genome = "".join(sequence_lines)
                if not genome: raise ValueError("Empty genome detected.")
                record = {"id": current_id, "genetic_payload": genome}
                records.append(record)

            # Grab New Header. Note to remember; Since current id starts as None, the program will start down here.
            current_id = temp[1:].strip()
            if not current_id: raise ValueError("FASTA header is missing a phage identifier.")
            # Clear DNA
            sequence_lines = []

        elif current_id is not None:
            #Normalize the DNA (clean it) before appending.
            normalized_sequence = temp.strip().upper()
            
            #Loop through DNA to ensure valid nucleotides via IUPAC alphabet.
            for nucleotide in normalized_sequence:

                if nucleotide not in valid_nucleotides:
                    raise ValueError(f"Invalid Nucleotide detected: {nucleotide!r}")
            sequence_lines.append(normalized_sequence)
        else:
            raise ValueError("Malformed FASTA file detected.")

    # Outside of loop, so save final record!
    if current_id is not None:
        genome = "".join(sequence_lines)
        if not genome: raise ValueError("Empty genome detected.")
        record = {"id": current_id, "genetic_payload": genome}
        records.append(record)


    if not records: raise ValueError("Empty FASTA file detected.")
    return records
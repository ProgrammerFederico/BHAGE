def parse_fasta(file):

    records = []
    current_id = None
    description = None
    sequence_lines = []
    valid_nucleotides = set("ACGTRYSWKMBDHVN")
    

    for temp in file:
        # Check for Header
        if temp.startswith(">"):

            # Check for new Header
            if current_id is not None:
                # Save previous header / DNA
                record = {"id": current_id, "genetic_payload": ''.join(sequence_lines)}
                records.append(record)

            # Grab New Header. Note to remember; Since current id starts as None, the program will start down here.
            current_id = temp[1:].strip()
            if not current_id: raise ValueError("FASTA header is missing a phage identifier.")
            # Clear DNA
            sequence_lines = []
        elif current_id is not None:
            normalized_sequence = temp.strip().upper()
            for nucleotide in normalized_sequence:
                if nucleotide not in valid_nucleotides:
                    raise ValueError("Invalid Nucleotide Detected.")
            sequence_lines.append(normalized_sequence)
        else:
            raise ValueError("Malformed FASTA File Detected.")

    if current_id is not None:
        record = {"id": current_id, "genetic_payload": ''.join(sequence_lines)}
        records.append(record)

    return records
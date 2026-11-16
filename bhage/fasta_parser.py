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
                # Save DNA
                record = {"id": current_id, "genetic_payload": ''.join(sequence_lines)}
                records.append(record)

            # Grab New Header
            current_id = temp[1:].strip()
            if not current_id: raise ValueError("FASTA header is missing a phage identifier.")
            # Clear DNA
            sequence_lines = []
        elif current_id is not None:
            # Add DNA to list
            sequence_lines.append(temp.strip().upper())
            
        else:
            raise ValueError("Malformed FASTA File Detected.")

    if current_id is not None:
        record = {"id": current_id, "genetic_payload": ''.join(sequence_lines)}
        records.append(record)

    return records
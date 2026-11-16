def parse_fasta(file):

    records = []
    current_id = None
    description = None
    sequence_lines = []

    

    for temp in file:
        if temp.startswith(">"):

            if current_id is not None:
                record = {"id": current_id, "genetic_payload": ''.join(sequence_lines)}
                records.append(record)

            current_id = temp[1:].strip()
            if not current_id: raise ValueError("FASTA header is missing a phage identifier.")
            sequence_lines = []
        elif current_id is not None:
            sequence_lines.append(temp.strip().upper())
            
        else:
            raise ValueError("Malformed FASTA File Detected.")

    if current_id is not None:
        record = {"id": current_id, "genetic_payload": ''.join(sequence_lines)}
        records.append(record)

    return records
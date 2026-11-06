def parse_fasta(file):

    records = []
    current_id = None
    description = None
    sequence_lines = []

    

    for temp in file:
        if temp.startswith(">"):

            if current_id is not None:
                record = {"id": current_id, "genetic_payload": sequence_lines}
                records.append(record)

            current_id = temp[1:].strip()

        # Temporary pause, next step is to reset sequence lines when a new header is encountered.
        # else:
                #sequence_lines.append(temp)
                #sequence_lines = []





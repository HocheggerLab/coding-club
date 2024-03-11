class DnaSequence:
    STOP_CODONS = ['TAA', 'TAG', 'TGA']  # Class constant for stop codons

    def __init__(self, fasta_file):
        self.metadata = ''
        self.sequence = ''
        self.read_fasta(fasta_file)
        self.orf = self.find_longest_orf()

    def read_fasta(self, fasta_file):
        """Reads a FASTA file and updates the metadata and sequence attributes."""
        with open(fasta_file) as file:
            lines = file.read().split('\n')
            for line in lines:
                if line.startswith('>'):
                    self.metadata = line
                else:
                    self.sequence += line
        self.sequence = self.sequence.replace('\n', '')

    def find_longest_orf(self):
        """Finds and returns the longest ORF in the sequence."""
        orfs = []

        # Find all ATG indices (start codons)
        start_indices = []
        index = self.sequence.find('ATG')
        while index != -1:
            start_indices.append(index)
            index = self.sequence.find('ATG', index + 1)

        # For each start codon, find the first stop codon in frame
        for start_index in start_indices:
            for i in range(start_index, len(self.sequence), 3):
                codon = self.sequence[i:i+3]
                if codon in DnaSequence.STOP_CODONS:
                    orfs.append(self.sequence[start_index:i+3])
                    break

        # Find the longest ORF
        return max(orfs, key=len) if orfs else ''
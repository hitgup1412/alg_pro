def lcs_dna(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Initialize the LCS matrix
    lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the LCS matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

    # Retrieve the LCS by backtracking
    lcs = ""
    i = m
    j = n

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs = seq1[i - 1] + lcs
            i -= 1
            j -= 1
        elif lcs_matrix[i - 1][j] >= lcs_matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

def compare_sequences(file1, file2, file3, threshold=70):
    with open(file1, 'r') as f1:
        seq1 = f1.read().strip()

    with open(file2, 'r') as f2, open(file3, 'w') as f3:
        for line in f2:
            seq2 = line.strip()
            lcs = lcs_dna(seq1, seq2)
            similarity_percentage = (len(lcs) / len(seq1)) * 100

            if similarity_percentage >= threshold:
                f3.write(f"{seq1}\t{seq2}\t{lcs}\n")

    print("Comparison completed. Results saved to file.")

# Usage example:
compare_sequences('file1.txt', 'file2.txt', 'output.txt', threshold=70)


# Example usage
seq1 = "AGTACGCA"
seq2 = "TATGC"
lcs = lcs_dna(seq1, seq2)

print("Longest Common Subsequence:", lcs)

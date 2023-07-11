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

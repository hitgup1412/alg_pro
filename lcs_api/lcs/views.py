from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view

def lcs(seq1, seq2):
   
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

@api_view(['POST'])
def lcs(request):
    file1 = request.FILES['file1']
    file2 = request.FILES['file2']
    threshold = int(request.POST.get('threshold', 70))

    seq1 = file1.read().decode('utf-8').strip()

    results = []
    for line in file2:
        seq2 = line.decode('utf-8').strip()
        lcs = lcs_dna(seq1, seq2)
        similarity_percentage = (len(lcs) / len(seq1)) * 100

        if similarity_percentage >= threshold:
            results.append({'seq1': seq1, 'seq2': seq2, 'lcs': lcs})

    return JsonResponse({'results': results})

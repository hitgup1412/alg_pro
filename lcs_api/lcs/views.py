from django.http import JsonResponse
from rest_framework.decorators import api_view

from .lcs import lcs_dna

@api_view(['POST'])
def lcs(request):
    file1_path = request.data.get('file1_path')
    file2_path = request.data.get('file2_path')
    threshold = int(request.data.get('threshold', 80))

    # Read contents from file1
    with open(file1_path, 'r') as file:
        seq1 = file.read().strip()
    
    results = []
    with open('file3', 'w') as file:
        with open(file2_path, 'r') as file2:
            for line in file2:
                seq2 = line.strip()
                lcs = lcs_dna(seq1, seq2)
                similarity_percentage = (len(lcs) / len(seq1)) * 100

                if similarity_percentage >= threshold:
                    results.append({'person': seq1, 'parent': seq2, 'lcs': lcs})
                    file.write(f"{seq1}\t{seq2}\t{lcs}\n")

    return JsonResponse({'results': results})

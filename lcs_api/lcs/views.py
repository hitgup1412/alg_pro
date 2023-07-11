from django.http import JsonResponse
from rest_framework.decorators import api_view

from .lcs import lcs_dna
@api_view(['POST'])
def lcs(request):
    file1 = request.FILES['file1']
    file2 = request.FILES['file2']
    threshold = int(request.POST.get('threshold', 80))

    seq1 = file1.read().decode('utf-8').strip()

    results = []
    with open('file3' , 'w') as file:
        for line in file2:
            seq2 = line.decode('utf-8').strip()
            lcs = lcs_dna(seq1, seq2)
            similarity_percentage = (len(lcs) / len(seq1)) * 100

            if similarity_percentage >= threshold:
                results.append({'person': seq1, 'parent': seq2, 'lcs': lcs})
                file.write(f"{seq1}\t{seq2}\t{lcs}\n")
        
        

    return JsonResponse({'results': results})

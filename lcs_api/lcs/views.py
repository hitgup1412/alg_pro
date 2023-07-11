from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
from .lcs import lcs_dna

@api_view(['POST'])
def lcs(request):
    file1_path = request.data.get('file1_path')
    file2_path = request.data.get('file2_path')
    threshold = int(request.data.get('threshold', 80))
    if not file1_path or not file2_path:
        return  Response(' Sorry. Input path is empty. Resend your request using a valid path.')

    if not os.path.isfile(file1_path) or not os.path.isfile(file2_path) :
        return  Response('Sorry. Invalid input path or file does not exist. Resend your request using a valid path.')

    file1_extension = os.path.splitext(file1_path)[1]
    file2_extension = os.path.splitext(file2_path)[1]
    if file1_extension != '.txt' or file2_extension !=".txt":
        return  Response('This time you have to be sorry. Input file must be a text file with ".txt" format. ')


    # Read contents from file1
    with open(file1_path, 'r') as file:
        seq1 = file.read().strip()
    
    file3 = os.path.dirname(file1_path)
    file3 = os.path.join(file3 ,"file3.txt")
    results = []
    with open(file3, 'w') as file:
        with open(file2_path, 'r') as file2:
            for line in file2:
                seq2 = line.strip()
                lcs = lcs_dna(seq1, seq2)
                similarity_percentage = (len(lcs) / len(seq1)) * 100

                if similarity_percentage >= threshold:
                    results.append({'person': seq1, 'parent': seq2, 'lcs': lcs})
                    file.write(f"{seq1}\t{seq2}\t{lcs}\n")

    return JsonResponse({'results': results})

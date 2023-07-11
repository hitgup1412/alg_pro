import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .huffman import (
    build_frequency_table,
    build_huffman_tree,
    build_encoding_table,
    compress_file,
)

@api_view(['POST'])
def compress_file_view(request):
    file_path = request.data.get('file_path')

    if not file_path:
        return  Response(' Sorry. Input path is empty. Resend your request using a valid path.')

    if not os.path.isfile(file_path):
        return  Response('Sorry. Invalid input path or file does not exist. Resend your request using a valid path.')

    file_extension = os.path.splitext(file_path)[1]
    if file_extension != '.txt':
        return  Response('This time you have to be sorry. Input file must be a text file. ')

    with open(file_path, 'r') as file:
        text = file.read()

    if not text:
        return  Response('Az nazare man okeye vali file khali akhe??')

    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)

    compress_file(file_path, encoding_table)

    compressed_file_path = os.path.splitext(file_path)[0] + '.compressed'
    return Response({'message': f'File compressed successfully: {compressed_file_path}'})

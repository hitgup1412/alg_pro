import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .huffman import (
    
    decompress_file,
)

@api_view(['POST'])
def decompress_file_view(request):
    compressed_file_path = request.data.get('compressed_file_path')
    encoding_table_path = request.data.get('encoding_table_path')

    if not compressed_file_path:
        return Response('Compressed file path is empty. Resend your request using a valid path.')

    if not os.path.isfile(compressed_file_path):
        return Response('Invalid compressed file path or file does not exist. Resend your request using a valid path.')

    if not encoding_table_path:
        return Response('Encoding table path is empty.')

    if not os.path.isfile(encoding_table_path):
        return Response('Invalid encoding table path or file does not exist. Resend your request using a valid path.')

    file_extension = os.path.splitext(compressed_file_path)[1]
    if file_extension != '.compressed':
        return Response('Input file must be a compressed file. Resend your request using a valid path.')

    decompress_file(compressed_file_path, encoding_table_path)

    decompressed_file_path = os.path.splitext(compressed_file_path)[0] + '.txt'

    return Response({'message': f'File decompressed successfully: {decompressed_file_path}'})

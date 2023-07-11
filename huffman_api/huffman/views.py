from django.shortcuts import render

import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .huffman import (
    build_frequency_table,
    build_huffman_tree,
    build_encoding_table,
    compress_file,
    decompress_file,
)

@api_view(['POST'])
def compress_file_view(request):
    file_path = request.data.get('file_path')
    with open(file_path, 'r') as file:
        text = file.read()

    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)

    compress_file(file_path, encoding_table)

    compressed_file_path = os.path.splitext(file_path)[0] + '.compressed'
    return Response({'message': f'File compressed successfully: {compressed_file_path}'})


@api_view(['POST'])
def decompress_file_view(request):
    compressed_file_path = request.data.get('compressed_file_path')
    encoding_table_path = request.data.get('encoding_table_path')
    
    decompress_file(compressed_file_path, encoding_table_path)
    
    decompressed_file_path =os.path.splitext(compressed_file_path)[0]+'.txt'

    
    return Response({'message': f'File decompressed successfully: {decompressed_file_path}'})


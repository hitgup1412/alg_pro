# alg_pro
apis are implemented in django
# lcs:
    lcs_api - lcs - views.py

# huffman
    huffman_api - huffman - views.py


how to:

Compress a file: POST http://localhost:8000/api/compress/
        Request body: {"file_path": "/path"}
        Response: {"message": "File compressed successfully: /path.compressed"}

Decompress a file: POST http://localhost:8000/api/decompress/
        Request body: {"compressed_file_path": "/compressed_file", "encoding_table": {...}}
        Response: {"message": "File decompressed successfully: /path"}


# original alghorithms:
    the main directory
# some of references:
    http://sharif.ir/~shahram.khazaei/files/courses/algorithms/lecture10.pdf
    https://virgool.io/ikavan/prefix-code-%DA%86%DB%8C%D8%B3%D8%AA-rx7j08bfsjik
    https://virgool.io/ikavan/%DA%A9%D8%AF%D9%87%D8%A7%DB%8C-%D9%87%D8%A7%D9%81%D9%85%D9%86-%DA%86%D9%87-%D9%87%D8%B3%D8%AA%D9%86    %D8%AF-pqe02l5jhgn0

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

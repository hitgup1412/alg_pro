import os


class HuffmanNode:
    def __init__(self,freq, char=None ):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(text):
    frequency_table = {}
    for char in text:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table

def build_huffman_tree(frequency_table):
    nodes = [HuffmanNode( freq,char) for char, freq in frequency_table.items()]
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = HuffmanNode(left.freq + right.freq)
        parent.left = left
        parent.right = right
        nodes.append(parent)
        
    return nodes[0]


def build_encoding_table(tree):
    encoding_table = {}

    def traverse_nodes(node, code):
        if node.char is not None:
            encoding_table[node.char] = code
            return

        traverse_nodes(node.left, code + '0')
        traverse_nodes(node.right, code + '1')

    traverse_nodes(tree, '')
    
    return encoding_table


def compress_file(file_path, encoding_table):
    # Read input file
    with open(file_path, 'r') as file:
        text = file.read()

    # Encode the text using the encoding table
    encoded_text = ''.join(encoding_table[char] for char in text)

    # Get the filename without extension
    file_name = os.path.splitext(file_path)[0]

    # Write the compressed data to a new file
    compressed_file_path = file_name + '.compressed'
    with open(compressed_file_path, 'w') as compressed_file:
        compressed_file.write(encoded_text)

    print(f'File compressed successfully: {compressed_file_path}')


def decompress_file(compressed_file_path, encoding_table):
    # Read the compressed file
    with open(compressed_file_path, 'r') as compressed_file:
        encoded_text = compressed_file.read()

    # Decode the encoded text using the encoding table (reverse lookup)
    decoding_table = {code: char for char, code in encoding_table.items()}
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in decoding_table:
            decoded_text += decoding_table[current_code]
            current_code = ''

    # Get the filename without the '.compressed' postfix
    decompressed_file_path = os.path.splitext(compressed_file_path)[0]

    # Write the decompressed data to a new file
    with open(decompressed_file_path, 'w') as decompressed_file:
        decompressed_file.write(decoded_text)

    print(f'File decompressed successfully: {decompressed_file_path}')

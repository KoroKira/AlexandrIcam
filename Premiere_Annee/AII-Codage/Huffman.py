# Huffman Coding Algorithm

def huffman_coding(data):
    # Create a frequency dictionary
    freq_dict = {}
    for char in data:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Create a priority queue and insert each character and its frequency
    p_queue = []  # Priority Queue
    for key, value in freq_dict.items():
        p_queue.append([value, [key, '']])
    p_queue.sort(reverse=True)

    # Build the Huffman Tree
    while len(p_queue) > 1:
        left_node = p_queue.pop()
        right_node = p_queue.pop()

        freq_sum = left_node[0] + right_node[0]
        node_list = [freq_sum, left_node[1] + right_node[1]]

        p_queue.append(node_list)
        p_queue.sort(reverse=True)

    # Traverse the Huffman Tree and assign codes to characters
    huffman_codes = {}
    traverse_tree(p_queue[0][1], huffman_codes)

    # Encode the data
    encoded_data = ''
    for char in data:
        encoded_data += huffman_codes[char]

    return encoded_data, huffman_codes


def traverse_tree(node_list, huffman_codes, code=''):
    if len(node_list) == 1:
        huffman_codes[node_list[0]] = code
    else:
        traverse_tree(node_list[0], huffman_codes, code + '0')
        traverse_tree(node_list[1], huffman_codes, code + '1')

# Huffman Decoding Algorithm

def huffman_decoding(data, huffman_codes):
    decoded_data = ''
    tmp = ''
    for bit in data:
        tmp += bit
        for key, value in huffman_codes.items():
            if tmp == value:
                decoded_data += key
                tmp = ''

    return decoded_data


if __name__ == "__main__":
    # Test Huffman Coding
    data = "The bird is the word"
    encoded_data, huffman_codes = huffman_coding(data)
    print("Encoded Data: ", encoded_data)
    print("Huffman Codes: ", huffman_codes)

    # Test Huffman Decoding
    decoded_data = huffman_decoding(encoded_data, huffman_codes)
    print("Decoded Data: ", decoded_data)

    def huffman_decoding(data, huffman_codes):
        decoded_data = ''
        tmp = ''
        for bit in data:
            tmp += bit
        for key, value in huffman_codes.items():
                if tmp == value:
                    decoded_data += key
                    tmp = ''

        return decoded_data
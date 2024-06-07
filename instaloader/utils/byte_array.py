def mp4_to_byte_array(file_path):
    with open(file_path, 'rb') as file:
        byte_array = file.read()
    return byte_array

def store_byte_array(byte_array, output_path):
    with open(output_path, 'wb') as file:
        file.write(byte_array)
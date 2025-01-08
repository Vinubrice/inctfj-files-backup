def fix_byte_swapping(input_file, output_file):
    with open(input_file, "rb") as infile:
        corrupted_data = infile.read()
    
    # Fix the swapping pattern
    fixed_data = bytearray()
    for i in range(0, len(corrupted_data), 2):
        if i + 1 < len(corrupted_data):  # Ensure there's a pair to swap
            fixed_data.append(corrupted_data[i + 1])  # Add the second byte first
            fixed_data.append(corrupted_data[i])      # Add the first byte second
        else:
            fixed_data.append(corrupted_data[i])      # Handle odd-length files
    
    with open(output_file, "wb") as outfile:
        outfile.write(fixed_data)

# Example usage
input_file = "chall.png"
output_file = "fixed.png"
fix_byte_swapping(input_file, output_file)
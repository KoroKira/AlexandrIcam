from itertools import product

def write_combinations_to_file(length, output_file_path):
    digits = [str(i) for i in range(16)]
    with open(output_file_path, 'w') as file:
        for combination in product(digits, repeat=length):
            file.write(''.join(combination) + '\n')

length_of_combination = 16
output_file_path = "resultat.txt"

write_combinations_to_file(length_of_combination, output_file_path)

print(f"Les combinaisons ont été écrites dans le fichier {output_file_path}")
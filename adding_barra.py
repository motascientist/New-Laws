with open("munincipios.txt", 'r') as municipalities:
    lines = municipalities.readlines()

new_lines = []

for line in lines:
    stripped_line = line.strip()  # Remove espaços em branco no início e no fim
    line_with_slash = stripped_line + '/'
    new_lines.append(line_with_slash)
    new_lines.append('\n')  # Adiciona uma linha em branco após cada URL

with open("munincipios.txt", 'w') as modified_file:
    modified_file.writelines(new_lines)

def replace_line_in_file(file_path, regex, replacement):
  new_lines = []

  with open(file_path, 'r') as f:
    for line in f:
      if regex.match(line):
        new_lines.append(replacement)
      else:
        new_lines.append(line)
  
  with open(file_path, 'w') as f:
    f.writelines(new_lines)
with open('filename.txt', 'w') as file: 
    file.write('\n'.join(iter(input, '')))
import os
import sys

def create_makefile():
    # Get the directory of the Python script
    py_program_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Get the directory name where the Python program resides
    dir_name = os.path.basename(py_program_dir)

    # Get a list of .c files in the Python program directory and its subdirectories
    c_files = []
    for root, dirs, files in os.walk(py_program_dir):
        for file in files:
            if file.endswith('.c'):
                c_files.append(os.path.relpath(os.path.join(root, file), py_program_dir))

    # Create the Makefile content
    makefile_content = (
        'NAME = ' + dir_name + '\n'
        'RM = rm -f\n'
        'CC = cc\n'
        'CFLAGS = -Wall -Werror -Wextra\n\n'
        'SRC = ' + ' \\\n\t'.join(c_files) + '\n\n'
        'OBJ = $(SRC:.c=.o)\n\n'
        'all: $(NAME)\n\n'
        '$(NAME): $(OBJ)\n'
        '\t$(CC) $(CFLAGS) $(OBJ) -o $(NAME)\n\n'
        'clean:\n'
        '\t$(RM) $(OBJ)\n\n'
        'fclean: clean\n'
        '\t$(RM) $(NAME)\n\n'
        're: fclean all\n'
    )

    # Write the Makefile content to a file
    with open('Makefile', 'w') as file:
        file.write(makefile_content)

# Call the function to create the Makefile
create_makefile()

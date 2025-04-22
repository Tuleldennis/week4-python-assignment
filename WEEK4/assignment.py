def read_and_modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read the contents of the file
            content = file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write the modified content to the new file
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_file}'")
    
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for input and output file names
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

# Call the function
read_and_modify_file(input_file, output_file)

# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and open 'my_file.txt' in write mode ('w')
        with open('my_file.txt', 'w') as file:
            # Write three lines of text to the file
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 12345\n")
            file.write("Finally, the third line of text.\n")
        print("File 'my_file.txt' created and content written successfully.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating/writing to the file: {e}")

    finally:
        print("File creation and writing process completed.")

def read_and_display_file():
    try:
        # Open 'my_file.txt' in read mode ('r')
        with open('my_file.txt', 'r') as file:
            # Read and display the contents of the file
            content = file.read()
            print("\nContent of 'my_file.txt':")
            print(content)
    
    except FileNotFoundError:
        print("File not found. Please ensure 'my_file.txt' exists.")
    
    except PermissionError:
        print("Permission denied. Cannot read the file.")

    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Open 'my_file.txt' in append mode ('a')
        with open('my_file.txt', 'a') as file:
            # Append three additional lines of text to the file
            file.write("This is an appended line.\n")
            file.write("Here is another appended line with number: 67890\n")
            file.write("Appending one more line of text.\n")
        print("Additional lines appended to 'my_file.txt' successfully.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to the file: {e}")

    finally:
        print("File appending process completed.")

# Execute the functions
create_and_write_file()
read_and_display_file()
append_to_file()
read_and_display_file()

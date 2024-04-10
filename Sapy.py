import json
import hashlib

# Function to generate a secure token using SHA-256
def generate_token(user_input):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Update the hash object with the user input
    hash_object.update(user_input.encode())
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# Function to save the token to a file
def save_token(user_id, token):
    # Create a dictionary to represent the user's token
    token_data = {'user_id': user_id, 'token': token}
    # Save the token data to a JSON file
    with open('user_tokens.json', 'a') as file:
        json.dump(token_data, file)
        file.write('\n')  # Add a newline to separate entries

# Modified function to generate assembly code, handle tokens, and save the code to a file
def generate_assembly_code(user_input, filename='assembly_code.asm'):
    processed_string = user_input.upper()
    # Generate a token for the user
    user_id = 'user123'  # Placeholder user ID
    token = generate_token(user_input)  # Use the user input for token generation
    # Save the token for the user
    save_token(user_id, token)
    # Generate the assembly code
    assembly_code = f"""
section .data
    output db '{processed_string}', 0
    userToken db 'Your token: {token}', 0

section .text
    global _start

_start:
    ; Print the processed string
    mov eax, 4
    mov ebx, 1
    mov ecx, output
    mov edx, {len(processed_string)}
    int 0x80

    ; Print the user's token
    mov ecx, userToken
    mov edx, {len('Your token: ') + len(token)}
    int 0x80

    ; Exit
    mov eax, 1
    int 0x80
    """
    # Save the assembly code to a file
    with open(filename, 'w') as file:
        file.write(assembly_code)
    print(f"Assembly code saved to {filename}")

# Read input from the user
user_input = input("Enter a string: ")

# Call the function to generate assembly code, handle tokens, and save the code
generate_assembly_code(user_input)

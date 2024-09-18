def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == '1':
            encrypt_menu()
        elif choice == '2':
            # decrypt_text()
            pass
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def encrypt_menu():
    text = """
▓█████  ███▄    █  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █     ███▄ ▄███▓▓█████  ███▄    █  █    ██ 
▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █    ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒
▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒   ▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░
▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒   ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░
░▒████▒▒██░   ▓██░▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░   ▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ 
░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ 
 ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ 
   ░      ░   ░ ░ ░          ░░   ░ ▒ ▒ ░░  ░░         ░       ▒ ░░ ░ ░ ▒     ░   ░ ░    ░      ░      ░      ░   ░ ░  ░░░ ░ ░ 
   ░  ░         ░ ░ ░         ░     ░ ░                        ░      ░ ░           ░           ░      ░  ░         ░    ░     
                  ░                 ░ ░                                                                                        
"""
    print(text)

    print("1. Encrypt Text")
    print("2. Back to Main Menu")

    choice = input("Choose an option: ")
    if choice == '1':
        encrypt_text()
    elif choice == '2':
        main()
    else:
        print("Invalid choice. Please try again.")

def encrypt_second_step(text, key):
    combined_logic = "a23b45c67d89e12f34g56h78i90j11k13l15m17n19o21p22q24r26s28t30u32v34w36x38y40z42A230B450C670D890E120F340G560H780I900J110K130L150M170N190O210P220Q240R260S280T300U320V340W360X380Y400Z4200R1S2T3U4V5W6X7Y8Z9A!$@%#^$&%*^(&)*_:?><:/>.?,/;'"


    encrypted_text = ""
    for char in text:
        if char in combined_logic:
            index = combined_logic.index(char)
            encrypted_text += combined_logic[(index + len(key)) % len(combined_logic)]
        else:
            encrypted_text += char

    return encrypted_text


def encrypt_text():
    text = input("Enter text to encrypt: ")
    
    # Encryption logic :
    key = input("Enter encryption key: ")
    first_step = f"0x{len(key)}"
    second_step = encrypt_second_step(text, key)
    phrase = f"{first_step}{second_step}"
    print(f"Encrypted text: {phrase}")

if __name__ == "__main__":
    main()
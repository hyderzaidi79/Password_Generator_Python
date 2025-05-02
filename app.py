import random
import string

print("🔐 Welcome to the Secure Password Generator!")
print("============================================\n")

def create_secure_password(core_word, total_length=12):
    if len(core_word) > total_length:
        print("⚠️ Your core word is longer than the desired password length!")
        return None

    extra_characters = string.ascii_letters + string.digits + string.punctuation
    
    remaining_chars = total_length - len(core_word)
    
    random_part = ''.join(random.choice(extra_characters) for _ in range(remaining_chars))
    
    full_password = list(core_word + random_part)
    
    random.shuffle(full_password)
    
    return ''.join(full_password)

core_word = input("📝 Enter a core word or base for your password: ")

length_input = input("🔢 Enter the total length of each password: ")

count_input = input("🔁 How many passwords would you like to generate? ")

if not length_input.isdigit() or not count_input.isdigit():
    print("❌ Please enter valid numbers for length and count.")
else:
    total_length = int(length_input)
    number_of_passwords = int(count_input)

    print("\n🔓 Your Generated Passwords:")
    print("-----------------------------")
    for i in range(number_of_passwords):
        password = create_secure_password(core_word, total_length)
        if password:
            print(f"{i + 1}. {password}")

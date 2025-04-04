from auth_core import register_user, authenticate_user
from otp_utils import generate_otp, send_otp, verify_otp
#from otp_utils import send_otp, verify_otp
from getpass import getpass

def main():
    print("=== OS-Level Secure Auth Module ===")
    print("1. Register")
    print("2. Login")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        email = input("Enter your email (used as username): ")
        password = getpass("Enter your password: ")
        success, message = register_user(email, password, email)  # passing email as both username and email

        print(message)

    elif choice == "2":
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        success, message = authenticate_user(email, password)
        if success:
            print("[*] Password Verified.")
            # OTP Verification
            otp = generate_otp()
            send_otp(email, otp)

            print(f"[+] OTP sent to {email}")

            entered = input("Enter the OTP: ").strip()
            if verify_otp(entered, otp):
                print("✅ Multi-Factor Authentication Success!")
            else:
                print("❌ OTP Verification Failed.")
        else:
            print(message)
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

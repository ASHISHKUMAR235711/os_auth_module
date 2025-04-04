import tkinter as tk
from tkinter import messagebox
from auth_core import register_user, authenticate_user
from otp_utils import generate_otp, send_otp, verify_otp
from getpass import getpass  # used only if fallback needed
import threading

def gui_register():
    def perform_registration():
        email = entry_email.get()
        password = entry_password.get()

        success, message = register_user(email, password)
        if success:
            messagebox.showinfo("Success", message)
            window.destroy()
        else:
            messagebox.showerror("Error", message)

    window = tk.Toplevel(root)
    window.title("Register")

    tk.Label(window, text="Email:").grid(row=0, column=0, padx=10, pady=10)
    entry_email = tk.Entry(window)
    entry_email.grid(row=0, column=1)

    tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(window, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(window, text="Register", command=perform_registration).grid(row=2, columnspan=2, pady=10)

def gui_login():
    def perform_login():
        email = entry_email.get()
        password = entry_password.get()

        success, message = authenticate_user(email, password)
        if not success:
            messagebox.showerror("Error", message)
            return

        messagebox.showinfo("Step 1 Success", "[*] Password Verified.\nNow verifying OTP...")

        # Simulate sending and verifying OTP
        otp = generate_otp()
        send_otp(email, otp)

        def verify():
            user_otp = entry_otp.get()
            if verify_otp(user_otp, otp):
                messagebox.showinfo("Success", "✅ Multi-Factor Authentication Success!")
                window.destroy()
            else:
                messagebox.showerror("Failed", "❌ OTP Verification Failed")

        otp_label = tk.Label(window, text="Enter OTP sent to your email:")
        otp_label.grid(row=3, column=0, padx=10, pady=10)
        entry_otp = tk.Entry(window)
        entry_otp.grid(row=3, column=1)

        tk.Button(window, text="Verify OTP", command=verify).grid(row=4, columnspan=2, pady=10)

    window = tk.Toplevel(root)
    window.title("Login")

    tk.Label(window, text="Email:").grid(row=0, column=0, padx=10, pady=10)
    entry_email = tk.Entry(window)
    entry_email.grid(row=0, column=1)

    tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(window, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(window, text="Login", command=perform_login).grid(row=2, columnspan=2, pady=10)

# === MAIN GUI ===
root = tk.Tk()
root.title("OS Auth Module GUI")

tk.Label(root, text="Secure Authentication Module", font=("Helvetica", 16, "bold")).pack(pady=20)

tk.Button(root, text="Register", width=20, command=gui_register).pack(pady=10)
tk.Button(root, text="Login", width=20, command=gui_login).pack(pady=10)

root.mainloop()

def gui_login():
    def perform_login():
        email = entry_email.get()
        password = entry_password.get()

        success, message = authenticate_user(email, password)
        if not success:
            messagebox.showerror("Error", message)
            return

        messagebox.showinfo("Step 1 Success", "[*] Password Verified.\nNow verifying OTP...")

        otp = generate_otp()
        send_otp(email, otp)

        # Show OTP input fields now
        otp_label.grid(row=3, column=0, padx=10, pady=10)
        entry_otp.grid(row=3, column=1)
        verify_btn.grid(row=4, columnspan=2, pady=10)

        def verify():
            user_otp = entry_otp.get()
            if verify_otp(user_otp, otp):
                messagebox.showinfo("Success", "✅ Multi-Factor Authentication Success!")
                window.destroy()
            else:
                messagebox.showerror("Failed", "❌ OTP Verification Failed")

        verify_btn.config(command=verify)

    window = tk.Toplevel(root)
    window.title("Login")

    tk.Label(window, text="Email:").grid(row=0, column=0, padx=10, pady=10)
    entry_email = tk.Entry(window)
    entry_email.grid(row=0, column=1)

    tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(window, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(window, text="Login", command=perform_login).grid(row=2, columnspan=2, pady=10)

    # Pre-create OTP widgets but keep them hidden
    otp_label = tk.Label(window, text="Enter OTP sent to your email:")
    entry_otp = tk.Entry(window)
    verify_btn = tk.Button(window, text="Verify OTP")


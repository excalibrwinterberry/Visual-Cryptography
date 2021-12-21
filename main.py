import tkinter as tk
import os
from encrypt import encrypthion
from decrypt import merging


def onClickEncrypt():
    # print(source_image.get())

    # get image source, secret message, destination folder
    img_source = source_image.get()
    secret_message = secret_msg.get()
    folder = foldername.get()
    key = int(encrypt_key.get())
    folder = folder + "/images"

    # create destination folder
    parent_dir = "/Users/arkaryan/Downloads"
    path = os.path.join(parent_dir, folder)
    os.makedirs(path)

    # create master and cipher share and save it to destination folder
    encrypthion.createSecrertMessage(secret_message, "Library/Fonts/Supplemental/Arial Unicode.ttf",
                                     path + "/secret.png")
    encrypthion.generateFromImage3(img_source, path + "/from_image.png", key)
    encrypthion.genereateCipherImage(path + "/secret.png", path + "/from_image.png", path + "/cipher.png")

    print("Encrypt")
    source_image.delete(0)
    secret_message.delete(0)
    foldername.delete(0)
    encrypt_key.delete(0)


def onClickDecrypt():
    # get master source, cipher source and destination folder
    cipher_image_source = cipher_image.get()
    master_image_source = master_image.get()
    folder = destination_folder.get()

    # create destination folder
    parent_dir = "/Users/arkaryan/Downloads"
    path = os.path.join(parent_dir, folder)
    os.makedirs(path)
    # generate merged image and save it to the destination folder

    merging.generateMergedImage(cipher_image_source, master_image_source, path + "/merged.png")
    print("Decrypt")

    cipher_image.delete(0)
    master_image.delete(0)
    destination_folder.delete(0)


root = tk.Tk()

root.title("Visual Cryptography: Encryption")
root.geometry('500x680+500+120')

encrypt_frame = tk.LabelFrame(root, text="Encrypt")
decrypt_frame = tk.LabelFrame(root, text="Decrypt")

encrypt_frame.pack(padx=5, pady=5)
decrypt_frame.pack(padx=5, pady=5)

lbl_source = tk.Label(encrypt_frame, text="Source of the image file", font=("Helvetica", 16)).grid(row=0, column=0,
                                                                                                   padx=10, pady=20)
source_image = tk.Entry(encrypt_frame, bd=1)
source_image.grid(row=0, column=1, columnspan=2, padx=10, pady=20)

lbl_secret_msg = tk.Label(encrypt_frame, text="Secret Message", font=("Helvetica", 16)).grid(row=1, column=0, padx=10,
                                                                                             pady=20)
secret_msg = tk.Entry(encrypt_frame, bd=1)
secret_msg.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

lbl_foldername = tk.Label(encrypt_frame, text="Folder Name", font=("Helvetica", 16)).grid(row=2, column=0, padx=10,
                                                                                          pady=20)
foldername = tk.Entry(encrypt_frame, bd=1)
foldername.grid(row=2, column=1, columnspan=2, padx=10, pady=20)

lbl_key = tk.Label(encrypt_frame, text="Key value", font=("Helvetica", 16)).grid(row=3, column=0, padx=10, pady=20)
encrypt_key = tk.Entry(encrypt_frame, bd=1)
encrypt_key.grid(row=3, column=1, columnspan=2, padx=10, pady=20)

tk.Button(encrypt_frame, text="Generate Master and Cipher share", command=onClickEncrypt, font=("Helvetica", 16)).grid(
    row=4, column=0, padx=10, pady=20, columnspan=3)

lbl_cipher_image = tk.Label(decrypt_frame, text="Source Cipher Image", font=("Helvetica", 16)).grid(row=0, column=0,
                                                                                                    padx=20, pady=20)
cipher_image = tk.Entry(decrypt_frame, bd=1)
cipher_image.grid(row=0, column=1, columnspan=2, padx=10, pady=20)

lbl_master_image = tk.Label(decrypt_frame, text="Source Master Image", font=("Helvetica", 16)).grid(row=1, column=0,
                                                                                                    padx=10, pady=20)
master_image = tk.Entry(decrypt_frame, bd=1)
master_image.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

lbl_destination_folder = tk.Label(decrypt_frame, text="Folder Name", font=("Helvetica", 16)).grid(row=2, column=0,
                                                                                                  padx=10, pady=20)
destination_folder = tk.Entry(decrypt_frame, bd=1)
destination_folder.grid(row=2, column=1, columnspan=2, padx=10, pady=20)

tk.Button(decrypt_frame, text="Generate Merged Image", command=onClickDecrypt, font=("Helvetica", 16)).grid(row=3,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=20,
                                                                                                            columnspan=3
                                                                                                            )

root.mainloop()

import os

old_file_name = "C:/Users/urosp/OneDrive/Dokumenti/Šola/Praksa-krka/uros.txt"
new_file_name = "C:/Users/urosp/OneDrive/Dokumenti/Šola/Praksa-krka/uros1.txt"

os.rename(old_file_name, new_file_name)

print("File renamed!")

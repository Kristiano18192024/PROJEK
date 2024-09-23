import time

while True:
    Data = "https://www.google.com"
    timestamp = int(time.time())
    file_name = f"/storage/emulated/0/Index_{timestamp}.txt"
    
    with open(file_name, "w") as file:
        file.write(Data)
        print(f"File {file_name} berhasil dibuat")
    
    time.sleep(0.05)
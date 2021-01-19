file_output = open("filename")

with  open("file_input", buffering=2000000) as file:
    for f in file:
        pass

file_output.close()
import re
#Programmes,Duration,Day fees,Distance Learning fees,Weekend fees
file = open("program_tuition.csv")
file_2 = open("program_tuition_raw.csv","a")
file_bytes = file.readlines()

for file_byte in file_bytes:
    #file_parts = re.split(r'(\\w<!\"\.),', str(file_byte))
    file_parts = file_byte.split(',"')#, str(file_byte))
    print(file_parts, f" with length: {len(file_parts)}")
    program_name = file_parts[0]
    day_tuition = file_parts[1]
    dl_tuition = file_parts[2]
    wkend_tuition = file_parts[3]

    day_string = f"{program_name} tuition fees day mode,\"{day_tuition}" if (day_tuition!="00")  else f"{program_name} tuition fees day mode,\"sorry day mode for {program_name} is not available\""
    file_2.write(day_string+"\n")

    dl_string = f"{program_name} tuition fees distance learning (DL) mode,\"{dl_tuition}" if (dl_tuition!="00")  else f"{program_name} tuition fees distance learning (DL) mode,\"sorry distance learning (DL) mode for {program_name} is not available\""
    file_2.write(dl_string+"\n")

    wkend_string = f"{program_name} tuition fees weekend mode,\"{day_tuition}" if (wkend_tuition!="00") else f"{program_name} tuition fees weekend mode,\"sorry weekend mode for {program_name} is not available\""
    file_2.write(wkend_string+"\n")

    print(day_string)
    print(dl_string)
    print(wkend_string)
start_char=ord('!')
end_char=ord('~')

for ascii_value in range(start_char,end_char+1): 
    char=chr(ascii_value)
    #print(f"Character: {char}, ASCII Decimal: {ascii_value}, ASCII Hexadecimal :0x{ascii_value:02X} ",end="\t")
    print(f" {ascii_value},0x{ascii_value:02X} ",end="\t")

    if (ascii_value - start_char +1)%5==0: 
        print()
        
        
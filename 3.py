def generate_pattern(size):
    if size % 2 == 0:
        print("Please enter an odd number.")
    
    for i in range(size):
        row = ["-"] * size  
        row[i] = "*"        
        row[size - 1 - i] = "*"  
        print("".join(row))  
        
size = int(input("Enter an odd number for the pattern size: "))
generate_pattern(size)

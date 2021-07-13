

def main():
    y = 0
    def switch_case(num):
        nonlocal y
        match num:
            case 1:
                y = 3
                return "Hello"
            case 2:
                y = 9
                return "Goodbye"
            case _:
                y = 0
                return "invalid choice"
    num = int(input("Please enter a number: "))
    print(switch_case(num))
    print ("The value of y is : "+ str(y))
    
if __name__ == "__main__":
        main()
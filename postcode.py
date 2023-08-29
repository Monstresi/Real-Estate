
def get_postcode():
    postcode = input("Enter your postcode: ")
    return postcode

def main():
    postcode = get_postcode()
    while len(postcode) != 4:
        postcode = get_postcode()

    print(f"Your postcode is {postcode}")
    exit()


main()

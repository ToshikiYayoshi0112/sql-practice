def main():
    # f = open("users.txt", mode = "r")
    #
    # text = f.read()
    #
    # print(text)
    #
    # f.close()

    with open("users.txt", mode="r") as f:
        text = f.read()

    print(text)

    print(f.closed)


if __name__ == "__main__":
    main()

import base64


def main():
    inp = input("->")
    # encoded the input (we need a bytes like object)
    encoded = inp.encode("utf-8")
    a85encoded = base64.a85encode(encoded)  # a85encoded the encoded string
    print(a85encoded)
    print(base64.a85decode(a85encoded).decode("utf-8"))  # decoded it


if __name__ == "__main__":
    main()

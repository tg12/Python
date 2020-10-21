'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



def encrypt(input_string: str, key: int) -> str:
    result = ''
    for x in input_string:
        if not x.isalpha():
            result += x
        elif x.isupper():
            result += chr((ord(x) + key - 65) % 26 + 65)
        elif x.islower():
            result += chr((ord(x) + key - 97) % 26 + 97)
    return result


def decrypt(input_string: str, key: int) -> str:
    result = ''
    for x in input_string:
        if not x.isalpha():
            result += x
        elif x.isupper():
            result += chr((ord(x) - key - 65) % 26 + 65)
        elif x.islower():
            result += chr((ord(x) - key - 97) % 26 + 97)
    return result


def brute_force(input_string: str) -> None:
    key = 1
    result = ''
    while key <= 94:
        for x in input_string:
            indx = (ord(x) - key) % 256
            if indx < 32:
                indx = indx + 95
            result = result + chr(indx)
        print(f'Key: {key}\t| Message: {result}')
        result = ''
        key += 1
    return None


def main():
    while True:
        print(f'{"-" * 10}\n Menu\n{"-", * 10}')
        print(*["1.Encrpyt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep='\n')
        choice = input("What would you like to do?: ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set between 0-25: "))
            if key in range(1, 95):
                print(encrypt(input_string.lower(), key))
        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("Please enter the string to be decrypted: ")
            brute_force(input_string)
            main()
        elif choice == "4":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()

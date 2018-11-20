import sys
import zipfile


def crack(x, y):
    password = None
    file_to_open = zipfile.ZipFile(x)
    with open(y, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            try:
                file_to_open.extractall(pwd=password)
                password = ('Password found: %s' % password)
                print(password)
            except:
                pass


def main():
    try:
        filename = sys.argv[1]
        wordlist = sys.argv[2]
        crack(filename, wordlist)
    except:
        print("\nUsage: python krackz.py <file> <wordlist>\n")
        print("Example: python krackz.py secret.zip wordlist.txt\n")


if __name__ == "__main__":
    main()

import argparse
from spiral_cipher import SpiralCipher, encode, decode

def main():
    parser = argparse.ArgumentParser(description="Spiral Cipher CLI")
    subparsers = parser.add_subparsers(dest="action", required=True)

    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode text or file")
    encode_parser.add_argument("input", help="Text or input file path")
    encode_parser.add_argument("-k", "--key", type=int, default=1, help="Encryption key")
    encode_parser.add_argument("-f", "--file", action="store_true", help="Treat input as file")
    encode_parser.add_argument("-o", "--output", help="Output file path")

    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Decode text or file")
    decode_parser.add_argument("input", help="Text or input file path")
    decode_parser.add_argument("-k", "--key", type=int, default=1, help="Encryption key")
    decode_parser.add_argument("-f", "--file", action="store_true", help="Treat input as file")
    decode_parser.add_argument("-o", "--output", help="Output file path")

    args = parser.parse_args()

    cipher = SpiralCipher(key=args.key)

    if args.action == "encode":
        if args.file:
            cipher.encrypt_file(args.input, args.output)
        else:
            print(encode(str(args.input), args.key))
    elif args.action == "decode":
        if args.file:
            cipher.decrypt_file(args.input, args.output)
        else:
            print(decode(str(args.input), args.key))

if __name__ == "__main__":
    main()
import base64
import os
import argparse
import logging

# Function to generate a salt
def generate_salt(length=16):
    return base64.urlsafe_b64encode(os.urandom(length)).decode('utf-8')


def main():
    """
    Generate a salt.
    Args:
        -l, --length (int): Length of the salt (default: 16)
    Raises:
        Exception: If an error occurs during salt generation.
    Returns:
        str: The generated salt.
    """
    parser = argparse.ArgumentParser(description='Generate a salt')
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the salt')
    args = parser.parse_args()

    try:
        salt = generate_salt(args.length)
        print(salt)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    main()

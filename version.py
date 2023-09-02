import argparse

# Define the version number
__version__ = "4.0.0"


def version():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    version()

@contextmanager
def manage_file(file_path, mode):
    file = None
    try:
        file = open(file_path, mode)
        yield file
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if file is not None:
            file.close()


with manage_file("example.txt", "w") as file:
    file.write("Hello, this is an example.")
    file.hdhd

print(file.closed)
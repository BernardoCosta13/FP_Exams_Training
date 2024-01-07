def readFileWithMax(fName, max_val: int) -> tuple[list[tuple[int, str, bool]], list[str]]:
    result = []
    errors = []

    try:
        with open(fName, "r") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split()

                    # Check if there are exactly two values in the line
                    if len(parts) != 2:
                        raise ValueError(f"Invalid number of values in line {line_number}: {line}")

                    # Extract values
                    x = line_number
                    y = parts[0]
                    z = int(parts[1]) < max_val

                    result.append((x, y, z))
                except ValueError as ve:
                    print(f"Error in line {line_number}: {ve}")
                    errors.append(f"Error in line {line_number}: {ve}")
                    continue  # Move on to the next line

    except FileNotFoundError:
        print("There was a problem accessing the file")
        raise SystemExit
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise SystemExit

    return result, errors


print(readFileWithMax("new_file.txt", 500))


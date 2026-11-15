"""Student Attendance Cleaner.

Reads student names from attendance.txt, cleans them (strip extra
spaces, fix capitalization), removes duplicates and saves the sorted
unique list to attendance_clean.csv.

Input : attendance.txt  (one name per line)
Output: attendance_clean.csv (one name per line, sorted alphabetically)
"""

CSV_FILE = "attendance_clean.csv"
INPUT_FILE = "attendance.txt"


def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            raw_names = f.readlines()
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    original_count = len(raw_names)

    # Clean every name: remove extra spaces, fix capitalization.
    cleaned = [name.strip().title() for name in raw_names if name.strip()]

    # Set removes duplicates; sorted() puts names in alphabetical order.
    unique_students = sorted(set(cleaned))

    with open(CSV_FILE, "w", encoding="utf-8") as f:
        for name in unique_students:
            f.write(name + "\n")

    print(f"Original number of records: {original_count}")
    print(f"Unique student count: {len(unique_students)}")
    print("Cleaned Attendance List:")
    for name in unique_students:
        print(name)
    print(f"\nCleaned list saved to {CSV_FILE}.")


if __name__ == "__main__":
    main()

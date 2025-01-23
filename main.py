def get_number_of_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    character_count = {}

    for char in text.lower():
        if char not in character_count:
            character_count[char] = 0
        character_count[char] += 1

    return character_count


def main():
    book: str = "books/frankenstein.txt"
    with open(book) as file:
        file_contents = file.read()

    number_of_words: int = get_number_of_words(file_contents)
    character_counts: dict[str, int] = count_characters(file_contents)
    sorted_character_counts: list[tuple[str, int]] = sorted(
        character_counts.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of {book} ---")
    print(f"{number_of_words} words found in the document")
    for char, count in sorted_character_counts:
        if not char.isalpha():
            continue

        print(f"The '{char}' character was found {count} times")


if __name__ == "__main__":
    main()

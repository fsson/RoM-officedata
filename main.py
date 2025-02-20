import scripts.fetcher as fetcher
import scripts.cleaner as cleaner

def main():
    print("Fetching JSON data as file...")
    fetcher.create_json()

    print("Converting all JSON files into flat CSV...")
    cleaner.create_csv()

if __name__ == "__main__":
    main()
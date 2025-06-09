import json
import os

def get_small_file(file_path, output_dir="output", max_files=100, chunk_size=2):
    try:
        # Create output directory
        metadata_dir = os.path.join(output_dir, 'wsi')
        os.makedirs(metadata_dir, exist_ok=True)

        # Read JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Filter small files (< 1.28MB)
        small_files = sorted(
            [item for item in data],
            key=lambda x: x['file_size'],
            reverse=False
        )

        print(f"Total small files: {len(small_files)}")

        # Split into chunks
        chunks = [small_files[i:i + chunk_size] for i in range(0, len(small_files), chunk_size)]
        chunks = chunks[:max_files]  # Limit number of output files

        for i, chunk in enumerate(chunks):
            output_file = os.path.join(metadata_dir, f'pair_{i+1}.json')
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(chunk, f, indent=2)
            print(f"Created {output_file} with {len(chunk)} items")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    get_small_file(
        'download_data/metadata.cart.2025-06-09.json',
        'output'
    )

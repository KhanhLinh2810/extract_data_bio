import json
import os
from itertools import islice

def process_json_files(file1_path, file2_path, output_dir="output"):
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(output_dir + '/metadata.cart.2025-06-04-wsi', exist_ok=True)
        os.makedirs(output_dir + '/metadata.cart.2025-06-04-gen', exist_ok=True)

        # Read and parse both JSON files
        with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

        # Create dictionaries mapping case_id to single data item
        data1_dict = {item['associated_entities'][0]['case_id']: item for item in data1}
        data2_dict = {item['associated_entities'][0]['case_id']: item for item in data2}

        # Find common case_ids
        common_case_ids = set(data1_dict.keys()).intersection(set(data2_dict.keys()))

        # Get filtered data for common case_ids
        filtered_data1 = [data1_dict[case_id] for case_id in common_case_ids]
        filtered_data2 = [data2_dict[case_id] for case_id in common_case_ids]

        # Sort data to ensure consistent order
        filtered_data1.sort(key=lambda x: x['associated_entities'][0]['case_id'])
        filtered_data2.sort(key=lambda x: x['associated_entities'][0]['case_id'])

        # Split into chunks of approximately 50 items
        chunk_size = 50
        total_items = len(common_case_ids)
        num_full_chunks = total_items // chunk_size
        num_pairs = min(10, num_full_chunks) + (1 if total_items % chunk_size > 0 else 0)

        print(f"Total common case_ids: {total_items}")
        print(f"Creating {num_pairs} output file pairs")

        # Process chunks
        for i in range(num_pairs):
            start_idx = i * chunk_size
            # For the last pair, take all remaining items
            if i == 10 or (i == num_pairs - 1 and total_items % chunk_size > 0):
                chunk1 = filtered_data1[start_idx:]
                chunk2 = filtered_data2[start_idx:]
            else:
                chunk1 = filtered_data1[start_idx:start_idx + chunk_size]
                chunk2 = filtered_data2[start_idx:start_idx + chunk_size]

            # Write chunk to files
            output_file1 = os.path.join(output_dir + '/metadata.cart.2025-06-04-wsi', f'pair_{i+1}.json')
            output_file2 = os.path.join(output_dir + '/metadata.cart.2025-06-04-gen', f'pair_{i+1}.json')

            with open(output_file1, 'w', encoding='utf-8') as f1:
                json.dump(chunk1, f1, indent=2)
            with open(output_file2, 'w', encoding='utf-8') as f2:
                json.dump(chunk2, f2, indent=2)

            print(f"Created pair {i+1}: {output_file1} and {output_file2} with {len(chunk1)} items")

    except Exception as e:
        print(f"Error processing files: {e}")

# Example usage
if __name__ == "__main__":
    process_json_files(
        'metadata.cart.2025-06-04-wsi.json',
        'metadata.cart.2025-06-04-gen.json',
        'output'
    )

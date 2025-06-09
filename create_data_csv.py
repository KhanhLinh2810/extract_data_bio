import json
import os
from itertools import islice
import csv

# label tượng trưng, không cần thay đổi
def process_json_files(json_dir_path, default_label = 'gf'):
    try:
        # Lấy danh sách tất cả các tệp trong thư mục
        files = os.listdir(json_dir_path)

        # Lọc ra các tệp JSON
        json_files = [file for file in files if file.endswith('.json')]

        for json_file in json_files:
            json_file_path = os.path.join(json_dir_path, json_file)

            with open(json_file_path, 'r', encoding='utf-8') as f1:
                data1 = json.load(f1)
            
            output_csv = os.path.join(json_dir_path, f"{json_file.split('.')[0]}_dataset_csv.csv")

            with open(output_csv, mode="w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["case_id", "slide_id", "label"])

                for entry in data1:
                    slide_id = entry["file_name"]
                    case_id = entry["associated_entities"][0]["case_id"]
                    label = default_label
                    writer.writerow([case_id, slide_id, label])

            print(f"✅ Đã tạo file {output_csv} thành công.")

            # output_lines = []
            # with open(txt_path, "r") as txt_file:
            #     # Đọc header
            #     header = txt_file.readline()
            #     output_lines.append(header.strip())

            #     # Đọc và parse cả hai tệp JSON
                

            #     # Tạo từ điển ánh xạ case_id thành một mục dữ liệu duy nhất
            #     data1_dict = {item['file_id']: item for item in data1}

            #     # Lọc các hàng có giá trị id xuất hiện trong JSON
            #     for line in txt_file:
            #         cols = line.strip().split()  # Tách các cột
            #         if cols[0] in data1_dict:  # Kiểm tra xem id có tồn tại trong JSON không
            #             output_lines.append(line.strip())

            # # Ghi kết quả vào tệp mới
            # output_file_path = os.path.join(json_dir_path, f"{json_file.split('.')[0]}_filtered.txt")
            # with open(output_file_path, 'w') as output_file:
            #     for line in output_lines:
            #         output_file.write(f"{line}\n")

    except Exception as e:
        print(f"Error processing files: {e}")


# Example usage
if __name__ == "__main__":
    process_json_files(
        'output/wsi',
        # 'output/metadata.cart.2025-06-04-gen',
    )

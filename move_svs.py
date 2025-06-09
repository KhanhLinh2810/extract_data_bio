import os
import shutil

def move_all_svs_files(src_dir, dst_dir):
    """
    Di chuyển tất cả các file .svs từ src_dir (kể cả thư mục con) sang dst_dir.
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    count = 0
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".svs"):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_dir, file)

                # Nếu file đã tồn tại ở đích, đổi tên để tránh ghi đè
                if os.path.exists(dst_file):
                    base, ext = os.path.splitext(file)
                    i = 1
                    while os.path.exists(dst_file):
                        dst_file = os.path.join(dst_dir, f"{base}_{i}{ext}")
                        i += 1

                shutil.move(src_file, dst_file)
                count += 1
                print(f"Moved: {src_file} → {dst_file}")

    print(f"Total .svs files moved: {count}")

if __name__ == "__main__":
    move_all_svs_files("/content", "/content/extract_data_bio/svs")

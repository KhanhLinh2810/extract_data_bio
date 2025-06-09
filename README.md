1. tải các thứ

- tải công cụ https://gdc.cancer.gov/access-data/gdc-data-transfer-tool - để tải ảnh wsi
- tải model và để trong thư mục extract_data_bio https://drive.google.com/file/d/1DoDx_70_TLj98gTf6YTXnu4tFhsFocDX/view

2. lệnh tải dữ liệu ảnh wsi

- gdc-client.exe download -m "đường dẫn/data/output/metadata.cart.2025-06-04-wsi/pair_1_filtered.txt"

3. tìm các file được tải xuống ở đâu, cop hết tất cả các file sang thư mục svs

4. chuẩn bị môi trường:

- cd clam
- conda env create -f env.yml
- conda activate clam_latest

5. chạy lệnh này để tạo ra các patch: < nhớ cd clam >

- python create_patches.py --source ./../svs --save_dir ./../patch --patch_size 256 --step_size 256 --seg --patch

6. chạy lệnh này để chạy ra các feature token: < nhớ cd clam >

- python extract_features.py --data_dir ./..\patch --csv_path ./../output\metadata.cart.2025-06-04-wsi\pair_1_dataset_csv.csv --feat_dir features/TCGA-BRCA --batch_size 64 --model_name swin

5 -> đầy bộ nhớ -> xóa file svs -> 6 -> đầy bộ nhớ -> h5 -> chạy lại 6 một lần nữa -> nếu đầy bộ nhớ thì lại xóa h5 tiếp -> chạy bước 5, cứ lặp lại tới khi hết file svs -> chạy part khác.

nếu như mà đang chạy dở, mà báo đầy xong dừng, thì xóa cái file chạy dở đi. -> để dữ liệu đúng.

1. tải các thứ
- tải repo https://github.com/mahmoodlab/CLAM.git
- tải công cụ https://gdc.cancer.gov/access-data/gdc-data-transfer-tool - để tải ảnh wsi
- tải model và để trong thư mục extract_data_bio https://drive.google.com/file/d/1DoDx_70_TLj98gTf6YTXnu4tFhsFocDX/view


2. lệnh tải dữ liệu ảnh wsi 
- gdc-client.exe download -m "đường dẫn/data/output/metadata.cart.2025-06-04-wsi/pair_1_filtered.txt"

3. tìm các file được tải xuống ở đâu, cop hết tất cả các file sang thư mục svs 

4. chuẩn bị môi trường:
- cd clam
- conda env create -f env.yml
- conda activate clam_latest

4. chạy lệnh này để tạo ra các patch:
- python create_patches.py  --source ./../svs --save_dir ./../patch --patch_size 256 --step_size 256 --seg --patch

5. chạy lệnh này để chạy ra các feature token: chưa chạy tới :v

6. cấu trúc repo:
   ![{ACA78063-5724-4C25-B683-5D4238762963}](https://github.com/user-attachments/assets/80de2160-24ac-4783-85de-d7749ce54308)



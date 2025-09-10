## 📌 Giới thiệu
Chord là một **thuật toán định tuyến trong hệ phân tán ngang hàng (P2P)**, được thiết kế để ánh xạ và tìm kiếm khóa (key) một cách hiệu quả trong không gian vòng tròn (identifier circle).  
Mỗi node trong mạng sẽ quản lý một tập khóa và sử dụng **finger table** để tăng tốc độ tìm kiếm.

- Tham số **M**: xác định kích thước vòng (ring size = 2^M).  
- **Successor** của một key là node đầu tiên theo chiều kim đồng hồ có ID ≥ key.  
- Finger table giúp giảm độ phức tạp tìm kiếm từ O(N) xuống O(log N).

---

## ⚙️ Cách thực hiện
1. Xác định tham số `M` và danh sách node trong vòng.  
2. Xây dựng **finger table** cho từng node:  
   - Mỗi entry finger[i] = successor của `(node_id + 2^(i-1)) mod 2^M`.  
3. findNode key: bắt đầu từ một node, sử dụng finger table để tìm successor chịu trách nhiệm cho key.  

---

## 🧪 Test Cases
Chương trình hỗ trợ nhiều test case với **M khác nhau**, danh sách node khác nhau, và tập key khác nhau.  

Ví dụ **Test case 1**:
- M = 4 (ring size = 16)  
- Nodes = {1, 5, 7, 9, 12}  
- Keys tra cứu = {0, 3, 5, 8, 10, 11}  

| Key | Successor Node |
|-----|----------------|
| 0   | 1 |
| 3   | 5 |
| 5   | 5 |
| 8   | 9 |
| 10  | 12 |
| 11  | 12 |
---

## 📷 Kết quả minh họa
<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://github.com/user-attachments/assets/0ab9d306-6500-4db9-b3e4-ca140bb6367f" alt="Finger Table" width="45%" />
  <img src="https://github.com/user-attachments/assets/cf8d020c-5073-4130-aea5-014d1a9202ab" alt="Key Lookup" width="45%" />
</div>


---

## 🚀 Cách chạy chương trình
```bash
python chord_algo.py

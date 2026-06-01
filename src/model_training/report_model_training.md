
================================== Bài toán phân loại  ===================================

Tổng quan: Sử dụng mô hình Random Forest Classifier và XGBoost Classifier để dự đoán Aggregate Rating theo 3 khoảng phân loại: Thấp ( < 3 điểm)- Trung Bình (3.0 - 4.0 điểm) - Cao (>= 4.0 điểm)

Quy trình thực hiện : Tách tập dữ liệu sau xử lí thành tập Train và tập Test để huấn luyện mô hình. Lựa chọn các tham số phù hợp để mô hình không bị overfitting  

Kết quả thực nghiệm:

Chỉ số	                            Random Forest	XGBoost
Accuracy 	                        65.09%	        62.46%
Training/Testing Accuracy Gap	    0.0514	        0.0132
F1-Macro	                        0.6555	        0.6304
F1-Weighted	                        0.6528	        0.6241

Nhận xét chỉ số tổng quát: 
-Accuracy đạt 65%, ở mức tương đối ổn cho một bài toán phân loại 3 nhóm
-F1 Marco > F1 Weighted ở cả 2 mô hình, cho thấy mô hình dự đoán hiệu quả ở cả 3 nhóm.
-Training/Testing Accuracy Gap đều rất nhỏ ~ 5% cho thấy mô hình không bị học vẹt - overfitting

Nhận xét ma trận nhầm lẫn: 
-Cả 2 mô hình dự đều báo tốt ở nhóm Thấp và Cao, nhưng gặp khó khăn ở nhóm khúc Trung bình do chồng lấn dữ liệu.
-Tuy nhiên, đường chéo chính của ma trận vẫn khẳng định rằng mô hình đã học được quy luật phân loại tổng quát.
-Mô hình RandomForest nhỉnh hơn XGBoost ở nhóm Trung Bình và Thấp nhưng kém hơn một ít ở nhóm Cao

Nhận xét các đặc trưng quan trọng nhất:
-RandomForest xem Votes là yếu tố quan trọng nhất, theo sau là City. Trong khi đó XGBoost lại coi City là quan trọng nhất, rồi mới đến Votes
-Nguyên nhân do thuật toán dự đoán của 2 mô hình khác nhau


================================== Bài toán hồi quy  ===================================

Tổng quan: Sử dụng mô hình Random Forest Regressor và XGBoost Regressor để dự đoán giá trị Aggregate Rating dưới dạng biến liên tục (khoảng từ 0 đến 5)

Quy trình thực hiện : Tương tự như bài toán phân loại (Tách dữ liệu và điều chỉnh tham số cho mô hình)

Kết quả thực nghiệm:
Chỉ số	                                Random Forest	XGBoost
Mean Abs Error(MAE)	                    0.2592	        0.2544
Root Mean Sq E	                        0.3480	        0.3402
R - squared(R2)	                        0.6084	        0.6258
Training/Testing Accuracy R-squared	    0.0031	        0.051
Training/Testing Accuracy MAE	        0.0022	        0.0003

Nhận xét chỉ số tổng quát: 
-MAE đạt 0.26:  Mô hình dự báo sát thực tế, với sai số trung bình chỉ khoảng ±0.26 điểm trên thang điểm 5.
-RMSE đạt 0.34: Cho thấy mô hình không có sai số bất thường lớn
-R² đạt 62% chứng tỏ mô hình nắm được tốt quy luật dữ liệu với bối cảnh bài toán có dữ liệu phụ thuộc vào yếu tố cảm tính
-Độ lệch của R² và MAE rất nhỏ, cho thấy mô hình không bị overfiting

Đánh giá hiệu năng 2 mô hình hồi quy:
-Cả 2 mô hình đều có sai số tuân theo phân phối chuẩn với sai số trung bình cực kỳ gần 0. Điều này khẳng định tính khách quan, không bị thiên vị của mô hình, cho thấy đa số các dự đoán đều chính xác và các trường hợp sai lệch lớn là rất hiếm.
-Nhìn chung với bài toán hồi quy này, XGBoost nhỉnh hơn RandomForest 1 ít do có R-squared lớn hơn , thể hiện sự ưu thế hơn trong việc nắm bắt quy luật của dữ liệu.

Nhận xét các đặc trưng quan trọng nhất:
-Các đặc trưng ảnh hưởng nhất trong bài toán hồi quy của 2 mô hình tương tự như trong bài toán phân loại


================================== Bài toán gợi ý  ===================================

Tổng quan: Xây dựng thuật toán gợi ý nhà hàng dựa trên các đặc trưng của 
dữ liệu ban đầu

Quy trình thực hiện: Làm sạch dữ liệu gốc và gộp các đặc trưng thành một cột duy nhất.
Encoding cột đó thành các ma trận vector bằng kỹ thuật TF-IDF Vectorizor. Cuối cùng dùng thuật toán tính độ tương đồng Cosine (Cosine Similarity) để tính độ tương đồng giữa nhà hàng đang được chọn và các nhà hàng khác trong dữ liệu.

Kết quả thực nghiệm: 
Các nhà hàng được gợi ý có sự tương đồng cao về loại hình ẩm thực, tên nhà hàng và địa điểm so với lựa chọn gốc, minh chứng cho tính hiệu quả của phương pháp TF-IDF kết hợp Cosine Similarity.
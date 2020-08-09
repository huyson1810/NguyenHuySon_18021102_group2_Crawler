# Crawler_Data_First <br/>
Crawler Data DSKTlab assignment2 <br/>
1.Tin tức (chạy file kenh14_test.py) -Nguồn: https://kenh14.vn/<br/>
-Số lượng bài: 10k+<br/>
-Tốc độ: 300 bài / phút<br/>
-Trạng thái: đã chạy được đầy đủ <br/>
-Thu thập được: link , tiêu đề, tác giả, nguồn cung cấp, mô tả tóm tắt, tags, ngày xuất bản, nội dung<br/>
-Mô tả mã nguồn:<br/>
name :tên của spider<br/>
start_urls:page đầu tiên để crawl rồi từ page này lan sang page khác<br/>
Hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:<br/>
  Kiểm tra xem link đó có phải là link cần crawl không?<br/>
  Sau khi kiểm tra thì ghi lại data đã crawl ra file dạng text<br/>
<br/>
2.Thương mại điện tử (chạy file tgdd.py) <br/>
-Nguồn: https://www.thegioididong.com/ <br/>
... Phần này code em đang dính 1 số lỗi khi crawl nhiều link chưa chạy được , em đang sửa hoàn thiện ạ ... <br/>
-- code hiện tại đang chỉ thu được 1 link cụ thể qua file tgdd_t1.py --
-Số lượng bài:  <br/>
-Tốc độ:  bài / phút<br/>
-Trạng thái: đã chạy được 1 link cụ thể đầy đủ <br/>
-Thu thập được: link , tên sản phẩm , đánh giá trung bình, phân loại/hãng, giá cả, nguồn ảnh đại diện, mô tả ngắn gọn, mô tả thông tin sản phẩm cụ thể, quảng cáo <br/>

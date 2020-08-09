# Crawler_Data_First <br/>
Crawler Data DSKTlab assignment2 <br/>
1.Tin tức (chạy file kenh14_test.py) -Nguồn: https://kenh14.vn/<br/>
-Số lượng bài: 5k+ (file txt trong output) <br/>
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
 <br/>

-Số lượng bài: khoảng 2k sản phẩm (để máy chạy trong 1h) <br/>
-Tốc độ: khoảng hơn 30 sản phẩm / phút<br/>
-Trạng thái: đã chạy được hoàn thiện <br/>
-Thu thập được: link , tên sản phẩm , đánh giá trung bình, phân loại/hãng, giá cả, nguồn ảnh đại diện, giới thiệu sản phẩm, mô tả ngắn gọn, mô tả thông tin sản phẩm cụ thể, quảng cáo <br/>
Phần source code các chức năng tương tự như crawl news

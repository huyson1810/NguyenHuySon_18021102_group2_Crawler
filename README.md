# Crawler_Data_First <br/>
Crawler Data DSKTlab assignment2 <br/>
1.Tin tức -Nguồn: https://kenh14.vn/<br/>
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
2.Thương mại điện tử -Nguồn: https://www.thegioididong.com/ <br/>

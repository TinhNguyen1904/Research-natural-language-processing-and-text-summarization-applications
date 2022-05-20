# -*- coding: utf-8 -*-
"""Gensim.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I_8goPGN1bSalaiuOS86d1NUlExCM9uo
"""

# load thư viện
from gensim.summarization import summarize

# Tập dữ liệu
mytext = """
Trump cáo buộc đảng Dân chủ đang theo đuổi "nỗ lực đảo chính bất hợp pháp, mang tính đảng phái" khi tìm cách luận tội ông.

"Chính các người mới là phe can thiệp vào bầu cử Mỹ, phá vỡ nền dân chủ của đất nước và cản trở công lý. Điều này không là gì khác ngoài một nỗ lực đảo chính bất hợp pháp, mang tính đảng phái và sẽ thất bại nặng nề tại hòm phiếu, dựa trên tình hình gần đây", Tổng thống Mỹ Donald Trump viết trong lá thư dài 6 trang gửi Chủ tịch Hạ viện Nancy Pelosi vào hôm qua để chỉ trích cuộc điều tra luận tội của phe Dân chủ. 

Ông chủ Nhà Trắng viết thêm rằng bà Pelosi "đang biến hạ viện từ cơ quan lập pháp được kính trọng thành một phòng xử án của cuộc đàn áp đảng phái", đồng thời "gần như không thèm che giấu sự thù ghét" đối với ông. 

"Bằng cách thúc đẩy cuộc luận tội trái phép đó, các người đang vi phạm lời thề nhậm chức, phá vỡ lòng trung thành với hiến pháp và tuyên chiến với nền dân chủ Mỹ. Các người coi dân chủ là kẻ thù của chính mình", Trump viết.
Bức thư của Trump được gửi đi trong bối cảnh hạ viện, nơi đảng Dân chủ chiếm đa số, dự kiến bỏ phiếu vào hôm nay về các điều khoản luận tội Tổng thống Mỹ và khả năng cao sẽ thông qua để đưa Trump ra xét xử tại thượng viện. Ông gần như chắc chắn sẽ trở thành tổng thống Mỹ thứ ba trong lịch sử bị luận tội. 

Trước đó, Ủy ban Tư pháp Hạ viện đã thông qua hai điều khoản luận tội Trump, bao gồm lạm dụng quyền lực và cản trở quốc hội. Phe Dân chủ cáo buộc Trump thúc ép Ukraine điều tra cha con cựu phó tổng thống Mỹ Joe Biden, đối thủ của Trump trong cuộc bầu cử năm 2020, gây nguy hiểm cho hiến pháp Mỹ, an ninh quốc gia và tính công bằng của bầu cử. 

Trong khi đó, đảng Cộng hòa vẫn cố gắng bảo vệ Trump, khi lãnh đạo phe đa số tại thượng viện Mitch McConnell bác bỏ yêu cầu của đảng Dân chủ nhằm đề nghị 4 quan chức cũ và đương nhiệm ra làm chứng tại phiên tòa luận tội dự kiến diễn ra ở thượng viện vào tháng tới. 

Hạ viện Mỹ mở cuộc điều tra luận tội Trump từ tháng 9, sau khi một người tố giác giấu tên đệ đơn cáo buộc Tổng thống Mỹ dùng gói viện trợ quân sự để gây áp lực lên người đồng cấp Ukraine Volodymyr Zelensky. Tuy nhiên, Trump phủ nhận các cáo buộc và gọi cuộc điều tra luận tội là trò lừa bịp."""

mytext = open("giaoduc.txt").read()

# Độ dài đoạn text
len(mytext)

# Tóm tắt văn bản
summarize(mytext)

summary_txt = summarize(mytext)

# Độ dài văn bản tóm tắt
len(summary_txt)

# Nhận 70% kết quả tóm tắt
summarize(mytext,ratio=0.7)

#Cách tìm vị trí của văn bản được trích xuất
docx = summarize(mytext,ratio=0.7)

docx
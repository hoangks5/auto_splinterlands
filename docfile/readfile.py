# Cài thư viện docx bằng lệnh trên cmd: pip install python-docx
import docx
def __read__file__(name): # Hàm để đọc file đuôi .docx
        doc = docx.Document(name)  # name là tên của file cần đọc ví dụ "Exam.docx"
        data = ""
        fullText = []
        for para in doc.paragraphs: # Lệnh for đọc từng trang trong file docx.
            fullText.append(para.text) # Trong mỗi trang lấy dữ liệu văn bản text và thêm vào biến fullText
            data = '\n'.join(fullText) # Gộp các phần tử trong chuỗi thành 1 chuỗi duy nhất
        print(data) 
        return(data) # Trả về toàn bộ văn bản trong file docx

# Ví dụ đọc file IIBM_storage.docx
__read__file__('IBM_storage.docx')
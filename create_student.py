import os
import sys

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Trang của {name}</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-100 text-gray-800">
    <div class="max-w-3xl mx-auto mt-16 p-8 bg-white shadow-lg rounded-xl">
        <h1 class="text-3xl font-bold mb-4">Xin chào, {name}!</h1>
        <p class="mb-4 text-lg">Đây là trang web của bạn. Hãy chỉnh sửa file <code>index.html</code> để thay đổi nội dung.</p>
        <p class="text-gray-600">Bạn có thể thêm file HTML, CSS, JS… vào thư mục này.</p>
        <a href="README.md" class="text-blue-600 underline mt-6 inline-block">
            Xem hướng dẫn sử dụng GitHub Web và GitHub.dev
        </a>
    </div>
</body>
</html>
"""

README = """# Hướng dẫn chỉnh sửa website của bạn

Thư mục này là nơi chứa toàn bộ mã nguồn website của **{name}**.

Bạn có thể chỉnh sửa trực tiếp trên GitHub mà **không cần cài đặt phần mềm**.

---

## 🚀 1. Chỉnh sửa trực tiếp trên GitHub Web

1. Vào thư mục của bạn trên GitHub
2. Bấm vào file `index.html`
3. Nhấn nút **Edit this file** (biểu tượng cây bút)
4. Sửa nội dung HTML
5. Kéo xuống cuối trang → Nhập nội dung commit  
   Ví dụ:
```
Cap nhat giao dien
```

6. Nhấn **Commit changes**

GitHub sẽ tự động deploy website của bạn.

---

## ✨ 2. Mở VS Code Web bằng GitHub.dev

GitHub.dev là phiên bản VS Code chạy trên trình duyệt.

Có 2 cách mở:

### Cách 1 — NHẤN PHÍM `.` (dấu chấm)
Khi đang xem repo, chỉ cần nhấn: `.`

→ VS Code Web sẽ mở ngay.

### Cách 2 — đổi URL từ `github.com` thành `github.dev`

Ví dụ:

`https://github.com/EDU-TMATH/12X_2025_2026/sites/{name}`

Đổi thành:

`https://github.dev/EDU-TMATH/12X_2025_2026/sites/{name}`

---

## 📁 3. Thêm trang HTML mới

1. Chuột phải thư mục của bạn → **Add file**  
2. Chọn *Create new file*
3. Đặt tên file, ví dụ: `about.html`
4. Nhập nội dung HTML
5. Commit

---

## 🖼️ 4. Thêm ảnh, CSS, JS

- Bấm **Add file → Upload files**
- Kéo thả file từ máy lên
- Commit thay đổi

Ảnh có thể gọi trong HTML như:

```html
<img src="images/avatar.png">
```

⸻

🌐 5. Xem website của bạn

Giáo viên sẽ cung cấp đường dẫn dạng:

`https://<username>.pages.dev`

⸻

⚠️ Lưu ý quan trọng
- Chỉ chỉnh sửa trong thư mục của bạn
- Không xoá hoặc đổi tên file của người khác
- Mỗi lần sửa phải Commit để lưu
- Deploy tự động chạy sau mỗi commit

⸻

Chúc bạn học tốt và xây dựng website thật đẹp!
"""

def create_student(name):
    folder_path = f"sites/{name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Tạo index.html
    with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE_HTML.format(name=name))

    # Tạo README.md
    with open(os.path.join(folder_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(README.format(name=name))

    print(f"Đã tạo thư mục cho học sinh: {name}")
    print(f"- {folder_path}/index.html")
    print(f"- {folder_path}/README.md")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python create_student.py <tên_học_sinh>")
        sys.exit(1)

    student_name = sys.argv[1]
    create_student(student_name)

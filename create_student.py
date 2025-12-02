import os
import argparse

BASE = "sites"

def create_student_folder(name: str):
    # Chuẩn hoá tên thư mục
    folder_name = name.strip().replace(" ", "_").lower()
    path = os.path.join(BASE, folder_name)

    os.makedirs(path, exist_ok=True)

    index_path = os.path.join(path, "index.html")

    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Xin chào {name}!</title>

    <!-- TailwindCSS v4 (jsDelivr CDN) -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>

<body class="min-h-screen bg-gradient-to-br from-sky-100 via-white to-indigo-100 flex items-center justify-center p-4">
    <div class="max-w-lg w-full">
        <div class="bg-white/80 backdrop-blur shadow-xl rounded-2xl border border-slate-200 p-8 text-center">
            <h1 class="text-3xl md:text-4xl font-bold text-slate-800 mb-4">
                Xin chào, <span class="text-indigo-600">{name}</span>! 👋
            </h1>

            <p class="text-slate-600 mb-6">
                Đây là trang web mẫu của bạn, được tạo tự động bằng TailwindCSS v4.
            </p>

            <p class="text-slate-700 mb-6 leading-relaxed">
                Hãy chỉnh sửa file 
                <code class="px-2 py-1 bg-slate-100 rounded text-sm">sites/{folder_name}/index.html</code>
                để bắt đầu thực hành HTML/CSS/JS nhé! 🚀
            </p>

            <div class="flex flex-col items-center gap-1 text-sm text-slate-500">
                <span>Được tạo tự động bởi hệ thống lớp học 😊</span>
                <span class="text-xs">Bạn có thể thêm CSS hoặc JS của riêng mình.</span>
            </div>
        </div>
    </div>
</body>
</html>
""")

    print(f"✔ Đã tạo thư mục + index.html (Tailwind v4 CDN) cho: {name}  →  {path}")


def main():
    parser = argparse.ArgumentParser(
        description="Tạo thư mục và file index.html dùng TailwindCSS v4 (jsDelivr CDN)."
    )
    parser.add_argument(
        "students",
        nargs="+",
        help="Danh sách tên học sinh (vd: huy tuan 'Minh Anh')"
    )

    args = parser.parse_args()

    if not os.path.exists(BASE):
        os.makedirs(BASE)

    for student in args.students:
        create_student_folder(student)

    print("\n🎉 Hoàn thành tạo các trang học sinh với TailwindCSS v4 CDN!")


if __name__ == "__main__":
    main()

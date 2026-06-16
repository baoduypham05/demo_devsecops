import os

# Đây là lỗi Hardcoded Secret (Lộ mã bí mật) cực kỳ nguy hiểm
# Công cụ quét SAST chắc chắn sẽ nhảy dựng lên và bắt lỗi này!
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE-SUPER-SECRET-KEY"

def main():
    print("Ứng dụng đang khởi chạy...")
    print("Đang kết nối tới AWS Service...")

if __name__ == "__main__":
    main()
import yt_dlp
import os

def download_youtube_audio(video_url):
    try:
        # Đặt đường dẫn output cố định là C:\Logan
        output_path = r"C:\Logan"
        if not os.path.exists(output_path):
            print(f"Lỗi: Không tìm thấy thư mục {output_path}")
            return
            
        # Cấu hình yt-dlp
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'verbose': False
        }
        
        print(f"Đang tải xuống từ: {video_url}")
        print(f"File sẽ được lưu vào: {output_path}")
        print("Vui lòng đợi...")
        
        # Tải video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_title = info['title']
            video_ext = info['ext']
            
        full_file_path = os.path.join(output_path, f"{video_title}.{video_ext}")
        
        print(f"\nTải thành công!")
        print(f"File được lưu tại:")
        print(full_file_path)
        
        # Kiểm tra xem file có tồn tại không
        if os.path.exists(full_file_path):
            print("Đã kiểm tra: File tồn tại ✓")
            print(f"\nBạn có thể tìm thấy file tại: {output_path}")
        else:
            print("Cảnh báo: Không tìm thấy file sau khi tải!")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    VIDEO_URL = "https://www.youtube.com/watch?v=orL4tbYSF_Q&ab_channel=VNPoP"
    download_youtube_audio(VIDEO_URL)
    
    input("\nNhấn Enter để thoát...")
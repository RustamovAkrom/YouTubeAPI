import subprocess

def check_rtmp_stream(rtmp_url):
    try:
        # Используем ffprobe для проверки потока
        command = [
            'ffprobe',
            '-v', 'error',  # Отключаем вывод ненужной информации
            '-select_streams', 'v:0',  # Выбираем видеопоток
            '-show_entries', 'stream=codec_name',  # Показываем только кодек
            '-of', 'default=noprint_wrappers=1',  # Формат вывода
            rtmp_url
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Если поток доступен, вернется кодек видеопотока
        if result.returncode == 0:
            print(f"Stream is live, codec: {result.stdout.strip()}")
            return True
        else:
            print(f"Stream is not available: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Пример использования
rtmp_url = "rtmp://localhost/live/sdfjoiojweo3i4"
is_live = check_rtmp_stream(rtmp_url)
if is_live:
    print("Stream is live!")
else:
    print("Stream is offline or unavailable.")

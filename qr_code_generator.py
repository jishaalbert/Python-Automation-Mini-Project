import pyqrcode

youtube_url="https://www.youtube.com/watch?v=_uQrJ0TkZlc"
video_qr =pyqrcode.create(youtube_url)
video_qr.svg("video1.svg",scale=8)


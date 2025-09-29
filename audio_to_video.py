from moviepy import AudioFileClip,ImageClip

audio_clip=AudioFileClip("audio.mp3")
image_clip=ImageClip("background.jpg").with_duration(audio_clip.duration)

video=image_clip.with_audio(audio_clip)
video=video.resize(height=720).with_fps(24)

video.write_videofile("output_video.mp4",codec='libx264',audio_codec='aac')
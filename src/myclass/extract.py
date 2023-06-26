from moviepy.editor import VideoFileClip

class Extract():
    def __init__(self, video_path):
        self.clip = VideoFileClip(video_path)
        self.max_fps = self.clip.fps
        
    def gif_extract(self, output_path, fps=10):
        self.clip.write_gif(output_path, fps)

    def sound_extract(self, output_path):        
        self.clip.audio.write_audiofile(output_path)


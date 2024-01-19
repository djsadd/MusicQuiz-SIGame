from moviepy.editor import AudioFileClip


def cut(song, start_time, end_time):

    print(start_time, end_time)
    input_file = f"static/music/{song}"
    audio_clip = AudioFileClip(input_file)

    trimmed_audio = audio_clip.subclip(start_time, end_time)
    output_file = f"music/{song}"

    # SAVE
    trimmed_audio.write_audiofile(output_file)

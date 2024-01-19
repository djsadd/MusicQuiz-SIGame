from flask import Flask, render_template, request, redirect, url_for
from main import SpotifyAccount
from cut_music import cut
from pack_create import Generate
app = Flask(__name__)


def create_pack(di):
    Generate(1, di)
    Generate.create_round("1-й раунд")
    len_di = len(di)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/download", methods=["POST"])
def download():
    response = request.form
    lst_len = len(response)//3
    di = {}
    for i in range(lst_len):
        di[f"song"] = response[f"song_{i}"]
        di[f"start_time_"] = response[f"start_time_{i}"]
        di[f"end_time_"] = response[f"end_time_{i}"]
        cut(response[f"song_{i}"], response[f"start_time_{i}"], response[f"end_time_{i}"])
    create_pack(di)
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    spotify_playlist_id = request.form.get('url')
    spotify_client_id = request.form.get('client-id')
    spotify_secret_code = request.form.get('secret-id')
    # file = request.files['file']
    # if file.filename == '':
    #     return "No selected file"
    # try:
    #     start_time = int(request.form['start_time'])
    #     end_time = int(request.form['end_time'])
    # except ValueError:
    #     return "Invalid time format"
    # file.save(f"static/{file.filename}")
    #
    # print(start_time, end_time)
    # input_file = f"static/{file.filename}"
    # audio_clip = AudioFileClip(input_file)
    #
    # trimmed_audio = audio_clip.subclip(start_time, end_time)
    # output_file = f"{file.filename}"
    #
    # # SAVE
    # trimmed_audio.write_audiofile(output_file)
    obj = SpotifyAccount(playlist=spotify_playlist_id)
    obj.songs_download()
    return render_template('result.html', items=obj.get_list_song())


if __name__ == '__main__':
    app.run(debug=True)


from youtube_transcript_api import YouTubeTranscriptApi

video_id = "nOzW1zieR7w"
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)


def seconds_to_srt_time_format(seconds):
    """秒をSRTファイル形式の時間に変換するヘルパー関数"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"


# 日本語の字幕を取得し保存
transcript = transcript_list.find_transcript(['ja'])
transcript_data = transcript.fetch() #dictionaryのlist
with open("output_captions.srt", "w", encoding='utf-8') as file:
    for index, item in enumerate(transcript_data, start=1): #enumerate()反復
        start_time = seconds_to_srt_time_format(item['start'])
        end_time = seconds_to_srt_time_format(item['start'] + item['duration'])
        text = item['text'].replace('\n', '\n')  # 改行を保持
        # SRTフォーマットに従ってファイルに書き出す
        file.write(f"{index}\n")
        file.write(f"{start_time} --> {end_time}\n")
        file.write(f"{text}\n\n")

print("字幕が正常にSRT形式で保存されました。")
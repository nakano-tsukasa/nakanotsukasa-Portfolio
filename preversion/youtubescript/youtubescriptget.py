from youtube_transcript_api import YouTubeTranscriptApi

video_id = "T6QvkLCCNN0"
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

transcript = transcript_list.find_transcript(['en'])
transcript_data = transcript.fetch()

# print(type(transcript)) 
# <class 'youtube_transcript_api._transcripts.Transcript'>
# print(type(transcript_data))
# <class 'list'>
# print(transcript_data)
# [{'text': 'HIKAKIN', 'start': 0.719, 'duration': 3.0}, {'text': ～

# for transcript in transcript_list: #利用可能字幕確認
#     print(transcript.language_code)

with open('output_caption.txt','w',encoding='utf-8') as file:
    for item in transcript_data:
        text = item['text'].replace('\n',' ').replace('[音楽]','')
        file.write(text)

print('Success!')
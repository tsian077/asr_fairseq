from pydub import AudioSegment

# files                                                                       
# src = "transcript.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
audSeg = AudioSegment.from_mp3("Record.mp3")
audSeg.export(dst, format="wav")
import os
import docx2txt

path = os.getcwd()

files = [
    "AVM_69_m_2021_3_5_S1_Part2_audio.docx",
    "AVM_69_m_2021_3_5_S2_audio.docx",
    "AVM_69_m_2021_3_5_S3_audio.docx",
    "AVM_69_m_2021_3_5_S4_audio.docx",
    "AVM_69_m_2021_3_5_S5_audio.docx",
    "AVM_69_m_2021_3_5_S6_audio.docx",
    "AVM_69_m_2021_3_5_S7_audio.docx",
    "AVM_69_m_2021_3_5_S8_audio.docx",
    "AVM_69_m_2021_3_5_S9_audio_News.docx",
    "AVM_69_m_2021_3_5_S9_audio_SmallTalk.docx",
]

for f in files:
    text = docx2txt.process(f)
    with open("combined.txt", "a") as text_file:
        text_file.write(text)
        text_file.write("\n\n")

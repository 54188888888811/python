import requests
import re
import json
import subprocess
import os
import ffmpeg


# 只需输入网址，使用前建议修改cookies

def bilibili(uil, cookies):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        'Referer': 'https://www.bilibili.com/', 'cookie': cookies
    }
    response = requests.get(uil, headers=header)
    #print(response.text)
    play_info = re.findall('window.__playinfo__=(.*?)</script>', response.text)[0]
    json_data = json.loads(play_info)
    video_url = json_data['data']['dash']['video'][0]['baseUrl']  # 视频文件api接口
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']  # 音频文件api接口
    if input('获取音频 or 视频（1 or 2）') == '1':
        print(666)
        response2 = requests.get(audio_url, headers=header, stream=True)
        with open('C:\\Users\Administrator\Desktop\你的音频.m4s', 'wb') as f:
            for chunk in response2.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                if chunk:
                    f.write(chunk)
        ffmpeg.input('C:\\Users\Administrator\Desktop\你的音频.m4s').output(
            'C:\\Users\Administrator\Desktop\你的音频.mp3', format='mp3').run()
        os.remove("C:\\Users\Administrator\Desktop\你的音频.m4s")
    else:
        response1 = requests.get(video_url, headers=header, stream=True)  # 视频文件
        response2 = requests.get(audio_url, headers=header, stream=True)  # 音频文件
        with open('temp_video.m4s', 'wb') as f:
            # 逐块写入文件，避免内存占用过大
            for chunk in response1.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                if chunk:
                    f.write(chunk)
        with open('temp_audio.m4s', 'wb') as f:
            for chunk in response2.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                if chunk:
                    f.write(chunk)
        command = [
            'ffmpeg',
            '-y',  # 覆盖输出文件
            '-i', 'temp_video.m4s',  # 输入视频文件
            '-i', 'temp_audio.m4s',  # 输入音频文件
            '-c:v', 'copy',  # 视频复制，不重新编码
            '-c:a', 'aac',  # 音频编码为 AAC
            '-strict', 'experimental',  # 允许非标准选项
            '你的视频.mp4'  # 输出文件路径
        ]
        try:
            # 运行命令
            subprocess.run(command, check=True)
            print("视频和音频合并成功！文件目录为E:\\你的视频.mp4")
        except subprocess.CalledProcessError as e:
            print(f"合并失败：{e}")
        try:
            os.remove('temp_video.m4s')
            os.remove('temp_audio.m4s')
        except os.error as e:
            print(f'文件删除失败：{e}')


while True:
    uil = input('请输入bilibili视频链接：')
    # cookies= input('请输入cookies')
    cookies = "buvid_fp_plain=undefined; enable_web_push=DISABLE; rpdid=|(um~JlmRuJ~0J'u~kJ|uk|~m; historyviewmode=list; LIVE_BUVID=AUTO8717380479746040; enable_feed_channel=ENABLE; CURRENT_QUALITY=80; buvid_fp=dd28ce90377845b2054a5f30ea7db97d; fingerprint=4ed5fcbd5fcd689fabc44f09c138271f; DedeUserID=1795943053; DedeUserID__ckMd5=678d665a740148e3; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; buvid3=F2B6F86A-96C8-5DB9-0567-7447983898D842902infoc; b_nut=1751541742; _uuid=EB73ED87-4D2A-A853-11D5-DBB6BAB10673642253infoc; theme_style=dark; SESSDATA=a67e5c02%2C1770128215%2C842f7%2A82CjBcNRNvlCVt_RXQJA1t0BKRQRRp9smDLNSmfwgPQHQuSzf7Q47D6D2uofTU_98_AwcSVjFKekJJYXE5Yk02UmlRVElhQWFUSlJiaVBHQjFWYV9MVlRQV292RmtXRXJ4YmVJcGFtWXMwN3FEVlJDemFWU0FlZGZSdXBwMGxkeXRucVFFMnJfaWhRIIEC; bili_jct=77c45e618164c1b693d6fd537759cde4; sid=7sloa09c; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTY1MjU1NjYsImlhdCI6MTc1NjI2NjMwNiwicGx0IjotMX0.6TewHHFZOMsjuwDUbfuyuduQGtz11WwZywah-fwPfi8; bili_ticket_expires=1756525506; buvid4=DE124A8D-E6CB-EA2F-2AE6-18A0F425B7B740696-023070412-NH7Qrg7XI9Iw2hMcWEC/WQ%3D%3D; home_feed_column=5; browser_resolution=1429-641; bp_t_offset_1795943053=1106554025521709056; b_lsid=97D2E789_198F833DCAD; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; CURRENT_FNVAL=4048"
    bilibili(uil, cookies)

from __future__ import unicode_literals
import youtube_dl
import argparse


def main():
  # 主程序
  # 定义一个ArgumentParser实例:
  parser = argparse.ArgumentParser(
      prog='youtube_dl-quickstart',  # 程序名
      description='YouTube Video Downloader.',  # 描述
      epilog='Copyright(r), 2024'  # 说明信息
  )

  # 定义关键字参数
  parser.add_argument('-u',
                      '--url',
                      help='YouTube video url.')

  # 解析参数:
  args = parser.parse_args()

  ydl_opts = {
      # "cachedir": False
      # "format": "mp4[height>=?1080]" # 没有声音
      # "format": "bestvideo[height>=?1080]" # 没有声音
      "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
      "writesubtitles": True,
      # "writeautomaticsub": True,
      "postprocessors": [{
          "key": "FFmpegEmbedSubtitle"
      }]
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.url])


# 命令行运行
if __name__ == '__main__':
  main()

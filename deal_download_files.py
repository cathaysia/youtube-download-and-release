import os
from os import path

os.system('rm -rf result')
os.system('rm -rf sub')
os.mkdir('result')
os.mkdir('sub')

# 处理字幕
for dirpath, dirnames, filenames in os.walk("downloads"):
    for filename in filenames:
        if not filename.endswith('vtt'):
            continue
        filepath = path.join(dirpath, filename)
        # sed 命令在此处只能用双引号
        cmd = 'sed -i "1d" "%s"' % (filepath)
        print("[deal] %s with %s" % (filepath, cmd))
        os.system(cmd)
        os.rename(filepath, path.join('./sub', filename.replace('vtt', 'srt')))
    # 压缩字幕
    os.system('rar a -v1.5g result/sub.rar ./sub')

# 处理视频
for dirpath, dirnames, filenames in os.walk("downloads"):
    for filename in filenames:
        if not filename.endswith('mp4'):
            continue
        # 压缩视频文件
        os.chdir(dirpath)
        cmd = 'rar a -v1.5g "{rarfile}" "{sourcefile}"'.format(
            rarfile=path.join('../result', filename.replace('mp4', 'rar')),
            sourcefile=filename
        )
        print("[deal] %s with %s" % (path.join(dirpath, filename), cmd))
        os.system(cmd)
        # 删除视频文件
        os.unlink(filename)
        os.chdir('..')

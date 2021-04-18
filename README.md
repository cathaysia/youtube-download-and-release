最初这个项目是 https://github.com/hw431/github-actions-youtube-dl 的一个 fork ，但是原项目大量代码不符合本项目的预期，所以做了大量的重构，现在除了目录结构相符外，其他大部分都已经和以前不一样了。

# 说明

使用 Github Actions 从 Youtube 下载视频并放到 Release

# 使用

Fork 这个仓库并将 dl.conf 修改为你需要下载的视频的 URL，一个 URL 占一行。修改后提交，然后在 Github actions 里查看下载情况，每次 push 会创建一个 action。

一次下载的视频总大小不得超过 14GB。

如果你只需要下载字幕，可以手动将 dl.conf 中的 `--write-auto-sub` 取消注释。 

每个下载的视频都会被分卷为大小不超过 1.5 G 的压缩包内（Github 限制是 2GB） 。使用压缩包对于视频而言可能反而会导致体积增大，但是为了 actions 上传文件时会更改文件名，因此使用压缩很有必要。

# 注意

1. 如果你已经下载完视频了，不要忘记把 realses 中的视频给删掉。请 *善意* 使用 Github 给出的免费空间。
2. 视频的下载和字幕的下载是分离的，action 会尝试下载所有可用的字幕文件并打包在 sub.rar 文件中。如果没有字幕文件，会创建一个 64B 大小的空 rar 文件
3. Release 文件的上传是分多次的，所以你接受到邮件的时候文件可能还没有上传完，最好等到 action 结束再去下载
3. Release 文件的上传是分多次的，所以你接受到邮件的时候文件可能还没有上传完，最好等到 action 结束再去下载
4. 目前而言，在下载 youtube 视频的时候速度很可观，但是在从 P 站下载一些视频的时候速度比较慢。所有采用了 youtube-dl + aria2 下载的形式。但是对于一些网站而言，可以禁止使用多线程下载，此种情况下，可以将 `dl.conf` 的 `--external-downloader aria2c` 这一行注释掉。
5. 如果你想要使用 ffmpeg 将视频和字幕合成，那么你需要将字幕文件修改成下面这种形式：（字幕编码为 UTF-8 without BOM）

```
1
00:00:01.120 --> 00:00:09.220
Never, ever give up learning English, unless
```

# 鸣谢

- 感谢 Github 对 action 和 Release 宽松的限制，使得本项目可以实现
- 感谢 Youtobe-dl 提供的下载器，使得我们可以使用 Youtobe-dl 去下载喜欢的视频
- 感谢 marvinpinto 提供的 workflow 脚本，使我可以便捷地上传多个 assets
- 感谢 Rar 提供的软件，使我简化了分卷压缩包的创建
编程语言：
python3语言


需要：
安装numpy、PIL库；ffmpeg软件。


文件说明：
	getImage.py文件是将视频按帧截取图片存储在images文件夹中，需要用到ffmpeg软件，只要将ffmpeg文件夹的bin目录配置到电脑环境变量就行了。

	image2txt.py文件是将图片转化成txt文件集，封装成包不需要运行。

	play.py文件需要在终端命令行中运行调用image2txt包将images图片转化成txt文件集存储在txt文件夹中。


运行说明：
首先运行getImage.py代码将2.mp4视频按帧截取图片存储在images文件夹中；
最后在终端命令行中运行play.py文件即刻看到效果<因为代码需要在终端上面显示txt文件集>
终端命令：python play.py
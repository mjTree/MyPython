import sys, os
import image2txt
import time

def getTxt(imagePath, txtPath):
	img_count = 1
	while img_count <= len(os.listdir(imagePath)):
		imageFile = imagePath + str(img_count) + '.png'
		txtFile = txtPath + str(img_count) + '.txt'
		image2txt.image2txt(imageFile, txtFile)
		print('骚能程序员加载中： ' + str(img_count) + '%')
		img_count += 1

def play(txtPath):
	txt_count = 1
	while txt_count <= len(os.listdir(txtPath)):
		os.system('type ' + txtPath + str(txt_count) + '.txt')
		time.sleep(1.0/40)
		txt_count += 1
		os.system('cls')

if __name__ == '__main__':
	txt_dir_path = r'D:\zzz\a\txt' + '\\'
	img_dir_path = r'D:\zzz\a\images' + '\\'
	getTxt(img_dir_path, txt_dir_path)
	play(txt_dir_path)

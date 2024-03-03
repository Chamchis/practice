# 이미지 파일을 열고, 
# 현재 사이즈를 출력한 다음, 
# 사이즈를 반으로 줄인 후 저장하세요.

from PIL import Image

image = Image.open('Real_Madrid_CF.png') # 이미지 파일 열기

width, height = image.size
print('='*50)
print('이미지 사이즈 : ',width, "x", height) # 현재 사이즈 출력

n_width = width // 2 # 사이즈를 반으로
n_height = height // 2

image = image.convert('RGB') # 에러로 인해 RGB 형식으로 변경

image.save('half_size_image.jpg') # 저장


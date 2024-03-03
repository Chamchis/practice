# 디렉토리 내 모든 이미지에 대해 썸네일을 생성하고, 
# 각 이미지의 이름 옆에 "_thumbnail"을 추가하여 저장하세요. 
# 썸네일의 최대 크기는 100x100 픽셀로 설정하세요.

import os
from PIL import Image

# 이미지가 포함된 디렉토리 경로 (유니코드 에러로 인해 앞에 r 추가)
dir_path = r'C:\Users\junho\OneDrive\Desktop\workspace\personal_practice\24_03_03'

for image_name in os.listdir(dir_path):
    if image_name.endswith(".jpg") and image_name.endswith(".png") and image_name.endswith(".jpeg"):

        image_path = os.path.join(dir_path, image_name)
        
        image = Image.open(image_path)
        
        # 썸네일 크기 조정
        image.thumbnail((100, 100))
        
        # 이미지 파일 이름에 "_thumbnail" 추가
        thumbnail_image_name = image_name.split(".")[0] + "_thumbnail." + image_name.split(".")[1]
        
        # 썸네일 이미지 저장
        thumbnail_path = os.path.join(dir_path, thumbnail_image_name)
        image.save(thumbnail_path)
        
        print(f"{image_name}의 썸네일을 생성하여 {thumbnail_image_name}로 저장했습니다.")
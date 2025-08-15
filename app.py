import pandas as pd
import slab
#import deepai
import download
# อ่านไฟล์ CSV
df = pd.read_csv("prompt.csv")

# แสดงข้อมูลทีละบรรทัด
for index, row in df.iterrows():
    print(f"Prompt ID: {row['Prompt ID']}") # ID จาก column แรก
    # print(f"Prompt Text: {row['Prompt Text']}")
    id, url = slab.text_to_image(row['Prompt Text']) # Prompt จาก column สอง ส่งเข้าไปถาม AI ผ่าน API
    print(f"Image URL: {url}")
    download.download_image(url, f"images/{id}.png") # โหลดไฟล์ SAVE ที่ Folder ตามชื่อจาก API สร้างมา
    print("-" * 50) 

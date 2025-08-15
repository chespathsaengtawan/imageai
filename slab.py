#SLAB_API_KEY
import os
import requests
import json
import time
from dotenv import load_dotenv
load_dotenv()
def text_to_image(prompt=str):
    print(f"Converting text to image with prompt: {prompt}")
    API_KEY = os.getenv("SLAB_API_KEY") # API KEY จาก SERVER AI ให้เรา
    #print(f"API_KEY: {API_KEY}")
    url = "https://modelslab.com/api/v6/images/text2img" # URL สำหรับเรียก API SERVER AI ให้เรา
    # ข้อมูล prompt ข้อความที่จะให้สร้าง จากไฟล์ .csv แต่ละ AI จะไม่เหมือนกันห
    data = {
        "key": API_KEY,
        "model_id": "flux",
        "prompt": prompt,
        "samples": "1",
        "negative_prompt": "(worst quality:2), (low quality:2), (normal quality:2), (jpeg artifacts), (blurry), (duplicate), (morbid), (mutilated), (out of frame), (extra limbs), (bad anatomy), (disfigured), (deformed), (cross-eye), (glitch), (oversaturated), (overexposed), (underexposed), (bad proportions), (bad hands), (bad feet), (cloned face), (long neck), (missing arms), (missing legs), (extra fingers), (fused fingers), (poorly drawn hands), (poorly drawn face), (mutation), (deformed eyes), watermark, text, logo, signature, grainy, tiling, censored, nsfw, ugly, blurry eyes, noisy image, bad lighting, unnatural skin, asymmetry",
        "width": "768",
        "height": "1024",
        "clip_skip": "1",
        "enhance_prompt": "null",
        "guidance_scale": "7.5",
        "safety_checker": "yes"
    }
    #  headers 
    headers = {
    "key": API_KEY, 
    "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        result = response.json()
        return result["id"],result["output"][0] # ส่งค่า ID และ URL รูปภาพ กลับไปยังฟังก์ชันที่เรียก
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")

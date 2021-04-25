FROM ubuntu:latest

COPY requirements.txt /tmp/requirements.txt
RUN sudo apt-get update 
RUN sudo apt-get install -y python3 python3-pip git firefox-webdriver tesseract-ocr tesseract-ocr-rus 
RUN python3 -m pip install -r /tmp/requirements.txt
COPY lightshot_image_scraper.py
CMD ["python3", "lightshot_image_scraper.py"]

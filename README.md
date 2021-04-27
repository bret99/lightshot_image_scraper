This a simple tesseract based tool for investigating Lightshot images to find some secrets.
One need some pre-installed dependencies:

1. python3 modules => pytesseract pillow random selenium;
2. tesseract-ocr, tesseract-ocr-rus, geckodriver on your system;

One can substitute number of link symbols on string 43 in lightshot_image_scraper.py file to what one likes.
Also one can add another langs support. One should pre-install the relevant tesseract-ocr lang support.
One should be careful about the CPU and RAM utilization because this project is based on selenium and tesseract libs. 
Or docker run -it --rm foreh/lightshot_image_scraper /bin/bash -c 'python3 lightshot_image_scraper.py'

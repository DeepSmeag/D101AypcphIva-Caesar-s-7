# D101AypcphIva-Caesar-s-7
Personal project made to save time on a daily thing o' mine


!!!IMPORTANT!!!
In order for this code to work, there are some dependencies:
- first, this was written using Python 3.7.0 x64
    -> needed external libraries are selenium for chrome and PIL , if I missed something I will update.
- second, the engine for image-to-text recognition is Tesseract-OCR, available here https://github.com/tesseract-ocr/tesseract/wiki for download, the version used is tesseract v4.0.0-beta.1.20180608 but any 4.x.x future updates should work;
- third, the library used for image processing is OpenCV 3.4.2, but future versions should work as well ;
- fourth, you will need chromedriver available here http://chromedriver.chromium.org/ , version used by me is 2.42 (probably).
All code was written on a Windows 10 64bit machine, might be different for other OS.

How to use:
1. Open W101Trivia.py and change lines 24 and 28 with your respective credentials
2. Open that same file with python prompt
3. Wait for chrome page to load, then enter numbers 1-10 to choose starting quiz; this is a failsafe option in case something breaks on the way, it can happen but it works properly most of time time; if the need arises, you can simply pick up from where you left off and there will probably be no more errors.
4. Wait, the prompt and chrome page will close by themselves at the end.

There are several possible errors, will make a list if needed and the errors are provided cause I don't know all of them.

Note: VR cache warnings are no problem, they appear often but don't cause any errors.

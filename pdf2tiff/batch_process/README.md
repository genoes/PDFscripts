# pdf2tiff
## Export PDF pages as TIFF files

# Homebrew installation (MacOS)

### Requirements
* [Homebrew](https://brew.sh/ "Homebrew")
* [Python 3](https://docs.brew.sh/Homebrew-and-Python "Python 3 Homebrew Install")
* [pdf2image](https://pypi.org/project/pdf2image/ "pdf2image")
* [Poppler](https://formulae.brew.sh/formula/poppler "poppler")
* [tqdm](https://github.com/tqdm/tqdm "tqdm")

------------
# Anaconda installation (Windows 10)

### Requirements
* [Anaconda](https://www.anaconda.com/products/distribution#windows "Anaconda")
* [pdf2image](https://anaconda.org/conda-forge/pdf2image "pdf2image")
* [tqdm](https://github.com/tqdm/tqdm "tqdm")
* **Poppler**: (conda package no longer functional)
	1. Download the latest binary: http://blog.alivate.com.au/wp-content/uploads/2017/01/poppler-0.51_x86.7z
	1. Extract the downloaded .7z file into user directory: C:\Users\<user_name>\
		* Note: You will need to have the 7zip software for this.
	1. Add poppler to PATH:
		* Right click on "This PC" -> Properties -> Advanced System Settings -> Environment Variables
		* Add "C:\Users\<user_name>\poppler-0.51\bin" to the user's path.

------------

### Troubleshooting

#### Errors
* *raise Error("Destination path '%s' already exists" % real_dst)<br/>shutil.Error: Destination path './TIFFs/image.tif' already existsshutil.Error: Destination path './TIFFs/image.tif' already exists*
	* Reason: Duplicate image file(s) present in the TIFF output directory.
	* Solutions:
		1. Remove duplicates from output directory and rerun script....OR
		2. Remove completed PDF from source and rerun script.

* [*1]    #### killed     python3 pdf2tiff.py
/usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/lib/python3.9/multiprocessing/resource_tracker.py:216: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '*
	* Reason: Might be a memory load issue. This will likely occur when processing large PDFs.
	* Solution: The script will typically finish processing a file before it stops. Remove the completed PDFs from the source folder and run the script again.

* *PIL.Image.DecompressionBombError: Image size (437500000 pixels) exceeds limit of 178956970 pixels, could be decompression bomb DOS attack.*
	* Reason: At least one image in the PDF is too wide to output.
	* Solution: Manually reduce resolution or crop the oversized image and rerun script.

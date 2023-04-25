from pdf2image import convert_from_path
import os, shutil
try:
    os.makedirs('./TIFFs')
except FileExistsError:
    # directory already exists
    pass

pdf_file = input('\n'"Enter absolute path to PDF file: ").strip()
pages = convert_from_path(pdf_file)
img_file = pdf_file.replace(".pdf", "")

count = 0
for page in pages:
    count += 1
    tiff_file = img_file + "_" + str(count).zfill(3) + ".tif"
    page.save(tiff_file, dpi=(600, 600)), 'TIFF'
    shutil.move(tiff_file, './TIFFs')

print('\n'
'''
  ,-~~-.___.
 / |  '     \      "Finished!"
(  )         0
 \_/-, ,----'
    ====           //
   /  \-'~;    /~~~(O)
  /  __/~|   /       |
=(  _____| (_________|

''''\n')

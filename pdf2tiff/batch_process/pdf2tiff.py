from pdf2image import convert_from_path
from tqdm import tqdm
import os, shutil
try:
    os.makedirs('./TIFFs')
except FileExistsError:
    # directory already exists
    pass

source = input('\n'"Enter absolute path to PDF directory: ").strip()
print('\n' "Analyzing files..."'\n')

for filename in os.listdir(source):
    if filename.endswith('.pdf'):
        file = (os.path.join(source, filename))
        pages = convert_from_path(file)
        img_file = file.replace('.pdf', "")

        count = 0
        pbar = tqdm(pages, colour = 'green', bar_format = '{l_bar}{bar:20}{r_bar}{bar:-10b}')
        
        for page in pbar:
            pbar.set_description("Extracting tiffs from %s" % filename)
            count += 1
            tiff_file = img_file + "_" + str(count).zfill(3) + ".tif"
            page.save(tiff_file, dpi=(600, 600), compression = 'none', filetype = 'TIFF')
            shutil.move(tiff_file, './TIFFs')

print('\n'
'''
  ,-~~-.___.
 / |  '     \      "Done!"
(  )         0
 \_/-, ,----'
    ====           //
   /  \-'~;    /~~~(O)
  /  __/~|   /       |
=(  _____| (_________|

''''\n')

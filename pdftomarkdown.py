# pip install pymupdf
import fitz

# path to searchable PDF file
DIGITIZED_FILE = "./The Atlantic - October 2022.pdf"

# A4 size
a4_size = (612, 792)
a4_margin = (100, 100)

# OCR the PDF using the default 'text' parameter
page_number = 0
(page_from, page_to) = (62, 75)

with fitz.open(DIGITIZED_FILE) as doc:
    with open("converted.md",'w') as file:
        for page in doc:
            # page_number = page_number + 1
            page_number += 1
            for block in page.get_text("blocks"):
                (x0, y0, x1, y1, text, block_nr, block_type) = block
                # text = page.get_text("text")

                if page_from <= page_number <= page_to and block_type == 0:
                    valid_block = True

                    # Is within the main text (no footnote or page number)
                    valid_block &= x0 < a4_size[0]-a4_margin[0]
                    valid_block &= y0 < a4_size[1]-a4_margin[1]
                    valid_block &= x1 > a4_margin[0]
                    valid_block &= y1 > a4_margin[1]

                    if valid_block:
                        file.write(text)
                    else:
                        print("DISCARD: ", page_number, (x0, y0, x1, y1))
                        print(text)

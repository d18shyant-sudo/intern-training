from pathlib import Path
import pymupdf
import pytesseract
from PIL import Image
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
file_path = Path("Mountains-Extend.pdf")
docs = pymupdf.open(filename=file_path)
contents = ""
fixed_chunk = []
FIXED_CHUNK_SIZE = 200
recursive_chunk = []
RECURSIVE_CHUNK_SIZE =200
structure_chunk = {}
sub_headers = []
header =  None
sub_header = None
page_count = []
for i,doc in enumerate(docs):
    page = doc
    page_count.append(str(i+1))
    struc = page.get_text("dict")  
    for block in struc["blocks"]:
        for line in block["lines"]:
            for span in line["spans"]:
                if span["size"] == 18.0:
                    header = span["text"]
                    structure_chunk[header]= {}
                if span["size"] == 13.5:
                       sub_header = span["text"]
                       sub_headers.append(sub_header)
                       structure_chunk[header][sub_header] = []
                if span["size"] == 9.0:
                        sentence = span["text"]
                        structure_chunk[header][sub_header].append(sentence)
    pix = page.get_pixmap(dpi=400)
    pix.save(f"{file_path.stem}-Page-{i}.png")
    image = Image.open(f"{file_path.stem}-Page-{i}.png")
    text = pytesseract.image_to_string(image=image,lang="eng")
    contents += text
for i in range(0,len(contents),FIXED_CHUNK_SIZE):
    fixed_chunk.append([contents[i:i+FIXED_CHUNK_SIZE]])
# for i,chunks in enumerate(fixed_chunk):
#      chunks = chunks[0].replace("\n"," ")
#      print(f"Chunk {i}:",chunks)
#      print("Embeddings:",model.encode(chunks))
# print("\nFIXED CHUNK\n\n",fixed_chunk)
def counter(content):
    count = 0
    for i in content:
        count += 1
    return count
for content in contents.split("\n\n"):
    if content.endswith(".") :
        if counter(content=content) <=  RECURSIVE_CHUNK_SIZE:
            recursive_chunk.append([content])
        else:
            line_chunk=[] 
            for line in content.split("."):
                if counter(content=line) <=  RECURSIVE_CHUNK_SIZE:
                    line_chunk.append(line)
                else:
                    word_chunk = []
                    for word in line.split(" "):
                        if counter(content=word) <= RECURSIVE_CHUNK_SIZE:
                                word_chunk.append([word])
                    line_chunk.append(word_chunk)
            recursive_chunk.append(line_chunk)
# print("\nRECURSIVE CHUNK\n")
# for chunk in recursive_chunk:
#      print(f"\nChunk :\n{chunk}")
#      print(f"Embeddings :",model.encode(chunk))
# print("\nSTRUCTURE CHUNK\n\n")
# for key in structure_chunk[header].keys():
#      for line in structure_chunk[header][key]:
#         if line not in page_count:
#             print(f"Heading :{list(structure_chunk.keys())[0]}")
#             print(f"Sub Heading:{key}")
#             print(f"chunk:{line}\n")
#             print(f"Embeddings:",model.encode(line))
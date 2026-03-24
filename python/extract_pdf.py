import fitz
import sys

doc = fitz.open(r'd:\Files\knowledge\python\尚硅谷大模型技术之Python1.01773811578.pdf')

with open(r'd:\Files\knowledge\python\pdf_output.txt', 'w', encoding='utf-8') as f:
    f.write(f'Total pages: {len(doc)}\n')
    for i in range(len(doc)):
        text = doc[i].get_text()
        f.write(f'--- Page {i+1} ---\n')
        f.write(text)
        f.write('\n\n')

print("Done! Output saved to pdf_output.txt")

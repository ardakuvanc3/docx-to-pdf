from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(txt_path, pdf_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    c.drawString(30, height - 30, content)
    c.save()

def docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    content = "\n".join([p.text for p in doc.paragraphs])

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    c.drawString(30, height - 30, content)
    c.save()

def text_to_pdf_from_terminal(pdf_path):
    print("Lütfen PDF'e kaydetmek istediğiniz metni girin (bitirmek için 'EOF' yazın):")
    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)
    
    content = "\n".join(lines)
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    c.drawString(30, height - 30, content)
    c.save()

def main():
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. TXT veya DOCX dosyasını PDF'e dönüştürme")
    print("2. Terminalden metin girip PDF'e dönüştürme")
    choice = input("Seçiminiz (1/2): ")

    if choice == '1':
        file_path = input("Dönüştürmek istediğiniz dosyanın yolunu girin: ")
        pdf_path = input("Kaydedilecek PDF dosyasının yolunu girin (örneğin: C:\Desktop\output.pdf): ")
        
        if file_path.endswith('.txt'):
            txt_to_pdf(file_path, pdf_path)
            print(f"{file_path} başarıyla {pdf_path} olarak kaydedildi.")
        elif file_path.endswith('.docx'):
            docx_to_pdf(file_path, pdf_path)
            print(f"{file_path} başarıyla {pdf_path} olarak kaydedildi.")
        else:
            print("Desteklenmeyen dosya formatı. Lütfen .txt veya .docx dosyası seçin.")
    
    elif choice == '2':
        pdf_path = input("Kaydedilecek PDF dosyasının yolunu girin: ")
        text_to_pdf_from_terminal(pdf_path)
        print(f"Terminalden alınan metin başarıyla {pdf_path} olarak kaydedildi.")
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 girin.")

if __name__ == "__main__":
    main()

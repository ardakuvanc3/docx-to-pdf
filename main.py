from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

def txt_to_pdf(txt_path, pdf_path, title="Title", font_name="Helvetica", font_size=12, text_color=colors.black):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            content = file.read()

        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter

        # Başlık ekleme
        c.setFont(font_name, font_size + 4)
        c.setFillColor(colors.blue)
        c.drawString(30, height - 40, title)

        # İçerik ekleme
        text_object = c.beginText(30, height - 60)
        text_object.setFont(font_name, font_size)
        text_object.setFillColor(text_color)
        
        for line in content.split('\n'):
            if text_object.getY() < 30:
                c.drawText(text_object)
                c.showPage()
                text_object = c.beginText(30, height - 40)
                text_object.setFont(font_name, font_size)
                text_object.setFillColor(text_color)
            text_object.textLine(line)

        c.drawText(text_object)
        c.save()
        print(f"{txt_path} başarıyla {pdf_path} olarak kaydedildi.")
    except Exception as e:
        print(f"Hata: {e}")

def docx_to_pdf(docx_path, pdf_path, title="Title", font_name="Helvetica", font_size=12, text_color=colors.black):
    try:
        doc = Document(docx_path)
        content = "\n".join([p.text for p in doc.paragraphs])

        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter

        # Başlık ekleme
        c.setFont(font_name, font_size + 4)
        c.setFillColor(colors.blue)
        c.drawString(30, height - 40, title)

        # İçerik ekleme
        text_object = c.beginText(30, height - 60)
        text_object.setFont(font_name, font_size)
        text_object.setFillColor(text_color)
        
        for line in content.split('\n'):
            if text_object.getY() < 30:
                c.drawText(text_object)
                c.showPage()
                text_object = c.beginText(30, height - 40)
                text_object.setFont(font_name, font_size)
                text_object.setFillColor(text_color)
            text_object.textLine(line)

        c.drawText(text_object)
        c.save()
        print(f"{docx_path} başarıyla {pdf_path} olarak kaydedildi.")
    except Exception as e:
        print(f"Hata: {e}")

def text_to_pdf_from_terminal(pdf_path, title="Title", font_name="Helvetica", font_size=12, text_color=colors.black):
    try:
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

        # Başlık ekleme
        c.setFont(font_name, font_size + 4)
        c.setFillColor(colors.blue)
        c.drawString(30, height - 40, title)

        # İçerik ekleme
        text_object = c.beginText(30, height - 60)
        text_object.setFont(font_name, font_size)
        text_object.setFillColor(text_color)
        
        for line in content.split('\n'):
            if text_object.getY() < 30:
                c.drawText(text_object)
                c.showPage()
                text_object = c.beginText(30, height - 40)
                text_object.setFont(font_name, font_size)
                text_object.setFillColor(text_color)
            text_object.textLine(line)

        c.drawText(text_object)
        c.save()
        print(f"Terminalden alınan metin başarıyla {pdf_path} olarak kaydedildi.")
    except Exception as e:
        print(f"Hata: {e}")

def main():
    try:
        print("Yapmak istediğiniz işlemi seçin:")
        print("1. TXT veya DOCX dosyasını PDF'e dönüştürme")
        print("2. Terminalden metin girip PDF'e dönüştürme")
        choice = input("Seçiminiz (1/2): ")

        if choice == '1':
            file_path = input("Dönüştürmek istediğiniz dosyanın yolunu girin: ")
            pdf_path = input("Kaydedilecek PDF dosyasının yolunu girin (örneğin: C:\\Desktop\\output.pdf): ")
            title = input("Başlık girin: ")
            font_name = input("Font ismi girin (örneğin: Helvetica): ")
            font_size = int(input("Font büyüklüğü girin (örneğin: 12): "))
            text_color_input = input("Yazı rengi girin (örneğin: black, blue, red): ")
            text_color = getattr(colors, text_color_input.lower(), colors.black)

            if not os.path.isfile(file_path):
                print("Dosya bulunamadı. Lütfen doğru dosya yolunu girin.")
                return

            if file_path.endswith('.txt'):
                txt_to_pdf(file_path, pdf_path, title, font_name, font_size, text_color)
            elif file_path.endswith('.docx'):
                docx_to_pdf(file_path, pdf_path, title, font_name, font_size, text_color)
            else:
                print("Desteklenmeyen dosya formatı. Lütfen .txt veya .docx dosyası seçin.")
        
        elif choice == '2':
            pdf_path = input("Kaydedilecek PDF dosyasının yolunu girin: ")
            title = input("Başlık girin: ")
            print("Örnek fontları görmek için 'KAO' yazınız: ")
            font_name = input("Font ismi girin (örneğin: Helvetica): ")
            if(font_name == "KAO"):
                print("Örnek fontlar:")
                print("""
                    1. Helvetica
                    2. Times-Roman
                    3. Courier
                    4. Symbol
                    5. ZapfDingbats
                    """)
                font_name = input("Font ismi girin (örneğin: Helvetica): ")

            font_size = int(input("Font büyüklüğü girin (örneğin: 12): "))
            text_color_input = input("Yazı rengi girin (örneğin: black, blue, red): ")
            text_color = getattr(colors, text_color_input.lower(), colors.black)
            
            text_to_pdf_from_terminal(pdf_path, title, font_name, font_size, text_color)
        else:
            print("Geçersiz seçim. Lütfen 1 veya 2 girin.")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()

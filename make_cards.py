import glob
from PIL import Image, ImageDraw, ImageFont
from shutil import copyfile
import textwrap

# def draw_wrapped_text(d, text):
#     for line in textwrap.wrap(text, width=30):
#         # d.text()

def main(question_files, card_backs):
    # print(question_files)
    # print(card_backs)
    card_number = 1
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 16)
    for (question_file, card_back) in zip(question_files, card_backs):
        print(f"proccessing {question_file} {card_back}")
        with open(question_file) as qfile:
            lines = qfile.readlines()
            for i in range(len(lines)//2):
                Q = lines[i*2]
                A = lines[i*2+1]
                assert Q.startswith('Q:'), Q
                assert A.startswith('A:'), A
                img = Image.new('RGB', (211, 328), color = (0, 0, 0))
                d = ImageDraw.Draw(img)
                WIDTH=25
                txt = '\n'.join(textwrap.wrap(Q, width=WIDTH)) + '\n\n' + '\n'.join(textwrap.wrap(A, width=WIDTH))
                print(txt)
                d.text((10, 10), txt, font=fnt, fill=(255, 255, 255))
                img.save('card_fronts/card_{}_front.png'.format(card_number))
                copyfile(card_back, 'card_backs/card_{}_back.png'.format(card_number))
                card_number += 1

if __name__ == '__main__':
    main(sorted(glob.glob("level*.txt")), sorted(glob.glob("level_images/*.png")))

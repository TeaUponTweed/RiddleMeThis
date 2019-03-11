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
    wakka = 0
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 60)
    for (question_file, card_back) in zip(question_files, card_backs):
        print(f"proccessing {question_file} {card_back}")
        with open(question_file) as qfile:
            lines = qfile.readlines()
            for i in range(len(lines)//2):
                Q = lines[i*2]
                A = lines[i*2+1]
                assert Q.startswith('Q:'), Q
                assert A.startswith('A:'), A
                scale = 4
                img = Image.new('RGB', (211*scale, 328*scale), color = (0, 0, 0))
                d = ImageDraw.Draw(img)
                WIDTH=22
                txt = '\n'.join(textwrap.wrap(Q, width=WIDTH)) + '\n\n' + '\n'.join(textwrap.wrap(A, width=WIDTH))
                print(txt)
                d.text((23*scale, 23*scale), txt, font=fnt, fill=(255, 255, 255))
                img.save('card_fronts/card_{}_front.png'.format(card_number))

                back_im=Image.open(card_back)
                back_im = back_im.resize((211*scale, 328*scale), Image.ANTIALIAS)
                back_pxs = back_im.load()
                # print(back_pxs[0, wakka])
                assert back_pxs[0, wakka] == (0,0,0,255)
                back_pxs[0, wakka] = (1,1,1,255)
                wakka += 1

                back_im.save('card_backs/card_{}_back.png'.format(card_number))

                card_number += 1

if __name__ == '__main__':
    main(sorted(glob.glob("level*.txt")), sorted(glob.glob("level_images/*.png")))

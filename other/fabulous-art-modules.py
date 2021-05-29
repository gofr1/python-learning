
# pip install fabulous
from fabulous import text, image

print(text.Text('Super', color='#ffffff', shadow=True, skew=6))
print(image.Image('other/qr.png'))

# pip install art
import art

print(art.randart())
art.tprint("Super", "mix") 

print(art.text2art("Super", font='block'))

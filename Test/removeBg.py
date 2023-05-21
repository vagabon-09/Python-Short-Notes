from removeBg import remove
from PIL import Image
input_path = 'updated_logo.png'
output_path = 'new.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
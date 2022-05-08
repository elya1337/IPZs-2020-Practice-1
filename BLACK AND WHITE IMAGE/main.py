from PIL import Image

def edit_photo(input_image_path, output_image_path, size):
   orig_res = Image.open(input_image_path)
   res = orig_res.resize(size)
   res.save(output_image_path)
   color_image = Image.open(input_image_path)
   blackwhite = color_image.convert('L')
   blackwhite.save(output_image_path)

if __name__ == '__main__':
    edit_photo('загружено.jpg',
        '231.jpg', size=(900,900))
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

'''
getting the image from user
'''


def get_image():
    user_input = input('Enter directory of image: ')
    image_data = image.imread(user_input)
    return image_data


'''
make a matrix for shadow by changing color of the pic(except white) to gray
make the shadow bigger by multiplying it to the shear transformation matrix(λ = 0.07)
'''


def shadow_pic(pic_data):
    size = pic_data.shape
    new_pic = np.zeros((size[0], int(1.07 * size[1]) + 1, 3), dtype='uint8')
    for i in range(size[0]):
        for j in range(int(1.07 * size[1]) + 1):
            new_pic[i][j] = [255, 255, 255]
    for i in range(size[0]):
        for j in range(size[1]):
            if np.any(pic_data[i][j] < 250):
                y = (0.07 * i) + j
                new_pic[i][int(y)] = [95, 94, 93]
    return new_pic


'''
mixing the shadow pic and original pic and make the final pic
'''


def final_pic(pic_data, matrix):
    size = pic_data.shape
    for i in range(size[0]):
        for j in range(size[1]):
            if np.any(pic_data[i][j] < 250):
                matrix[i][j] = pic_data[i][j]

    plt.imshow(matrix)
    plt.show()


if __name__ == '__main__':
    pic_data = get_image()
    matrix = shadow_pic(pic_data)
    final_pic(pic_data, matrix)

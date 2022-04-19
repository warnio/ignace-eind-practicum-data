import glob
import numpy as np
import matplotlib.pyplot as plt


def preprocess_coords(coords):
    new_coords = []
    for x, y in coords.T:
        if 355 < y < 360 and 395 < x < 405 or x > 400:
            pass
        else:
            new_coords += [[x, y]]
    return np.array(new_coords).T


coord_files = sorted(glob.glob('./coords/*.npy'))
pairs = {}

for file in coord_files:
    base = '_'.join(file.split('_')[:-1])
    if base not in pairs:
        pairs[base] = [file]

    else:
        pairs[base] += [file]


for key, value in pairs.items():
    pairs[key] = [preprocess_coords(np.load(file)) for file in value] # load all the files in the list


def plot_coords(coords, c):
    coords = preprocess_coords(coords)
    x, y = coords[1, :], coords[0, :]
    new_x, new_y = [], []

    # only keep coordinates if the next set is within 100 pixels of the EMA of the previous coordinates
    for i in range(len(x)):
        if i == 0:
            new_x.append(x[i])
            new_y.append(y[i])
            moving_avg_x = x[i]
            moving_avg_y = y[i]
        else:
            if np.sqrt((x[i] - moving_avg_x)**2 + (y[i] - moving_avg_y)**2) < 30:
                new_x.append(x[i])
                new_y.append(y[i])
            else:
                print('welp, we tried')

        moving_avg_x = .9 * moving_avg_x + .1 * x[i]
        moving_avg_y = .9 * moving_avg_y + .1 * y[i]

    new_x, new_y = np.array(new_x), np.array(new_y)

    plt.plot(new_x, -1*new_y, c=c)


all_coords_green = np.concatenate([value[0] for value in pairs.values()], axis=1)
all_coords_purple = np.concatenate([value[1] for value in pairs.values()], axis=1)
print(len(all_coords_green), len(all_coords_purple))

# img = np.zeros((660, 360))
# for coord in all_coords_purple.T:
#     img[int(coord[0]), int(coord[1])] += 1
# img /= np.max(img)
# plt.imshow(img)
# plt.show()


for coord1, coord2 in list(pairs.values())[23:]:
    plot_coords(coord1, 'g')
    plot_coords(coord2, 'm')
    plt.show()
    print(coord1.shape, coord2.shape)
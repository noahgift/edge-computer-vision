import os
for name in ['training', 'testing']:
    with open('mnist_dataset_{}.csv'.format(name), 'w') as output_file:
        print('=== creating {} dataset ==='.format(name))
        output_file.write('image_path,label\n')
        for i in range(10):
            path = '{}/{}'.format(name, i)
            for file in os.listdir(path):
                if file.endswith(".png"):
                    output_file.write('{},{}\n'.format(os.path.join(path, file), str(i)))

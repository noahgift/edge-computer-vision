# Install Ludwig
python3 -m venv ~/.ludwig
source ~/.ludwig/bin/activate
pip install ludwig
pip install --upgrade pip
pip install ludwig

# Download the MNIST dataset
git clone https://github.com/myleott/mnist_png.git
cd mnist_png/
tar -xf mnist_png.tar.gz
cd mnist_png/

# Train Model
ludwig train \
  --data_train_csv mnist_dataset_training.csv \
  --data_test_csv mnist_dataset_testing.csv \
  --model_definition_file model_definition.yaml

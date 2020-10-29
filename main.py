import numpy as np


def get_dataset():
    """
    Method used to generate the dataset
    """
    # numbers of row per class
    row_per_class = 5
    # Genarate row
    print(np.ramdom.randint(row_per_class, 2))


if __name__ == "__main__":
    get_dataset()
    pass

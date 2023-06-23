import cv2
import numpy as np

def copy_move_detection(image, block_size=8):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the size of blocks
    block_h, block_w = block_size, block_size

    # Calculate the number of block rows and columns
    rows = gray.shape[0] // block_h
    cols = gray.shape[1] // block_w

    # Create a 2D array to store block hashes
    hashes = np.zeros((rows, cols), dtype=np.uint64)

    # Calculate block hashes using average intensity values
    for i in range(rows):
        for j in range(cols):
            block = gray[i * block_h:(i + 1) * block_h, j * block_w:(j + 1) * block_w]
            block_mean = np.mean(block)
            hashes[i, j] = hash(block_mean)

    # Find duplicate or copied blocks
    duplicates = []
    for i in range(rows):
        for j in range(cols):
            if hashes[i, j] != 0:
                for k in range(i + 1, rows):
                    for l in range(cols):
                        if hashes[i, j] == hashes[k, l]:
                            duplicates.append((i, j, k, l))

    # Highlight the detected copied regions
    result = image.copy()
    for duplicate in duplicates:
        i, j, k, l = duplicate
        x1, y1 = j * block_w, i * block_h
        x2, y2 = l * block_w + block_w, k * block_h + block_h
        cv2.rectangle(result, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Display the result
    cv2.imshow("Copy-Move Detection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the image
image = cv2.imread("image.jpg")

# Perform copy-move forgery detection
copy_move_detection(image)

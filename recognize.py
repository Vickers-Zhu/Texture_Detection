# import the necessary packages
import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
                help="path to the training images")
args = vars(ap.parse_args())

# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns.LocalBinaryPatterns(3, 1)
data = []
labels = []
# loop over the training images
for imagePath in paths.list_images(args["training"]):
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)

    # extract the label from the image path, then update the
    # label and data lists
    labels.append(imagePath.split("\\")[2])
    data.append(hist)

# train a Linear SVM on the data
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)
correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\bark1"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

# display the image and the prediction
# cv2.imshow("Image", image)
# cv2.waitKey(0)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\bark2"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\bark3"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\brick1"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\brick2"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\carpet1"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\carpet2"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\corduroy"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1

print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\floor1"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\floor2"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\fur"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\glass1"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\glass2"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\granite"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\knit"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\marble"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\pebbles"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
# loop over the testing images
for imagePath in paths.list_images("images\\testing\\plaid"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
      correct = correct + 1
print(correct)


correct = 0
for imagePath in paths.list_images("images\\testing\\upholstery"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
for imagePath in paths.list_images("images\\testing\\wall"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
for imagePath in paths.list_images("images\\testing\\wallpaper"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)



correct = 0
for imagePath in paths.list_images("images\\testing\\water"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
for imagePath in paths.list_images("images\\testing\\wood1"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)

correct = 0
for imagePath in paths.list_images("images\\testing\\wood2"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)


correct = 0
for imagePath in paths.list_images("images\\testing\\wood3"):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    print(prediction[0])
    if prediction[0] == imagePath.split("\\")[2]:
        correct = correct + 1
print(correct)
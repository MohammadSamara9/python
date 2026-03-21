image_dimensions = [
    (640, 480),
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1920, 1080)
]

print(image_dimensions[2][1])


image_filenames = [
    'img_001.jpg',
    'img_002.jpg',
    'img_003.jpg',
    'img_004.jpg',
    'img_005.jpg',
    'img_006.jpg'
]
print(image_filenames[-3:])


image_classifications = ['dog', 'cat', 'bird', 'cat', 'dog']
is_palindrome = (image_classifications == image_classifications[::-1])
print(is_palindrome)




a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))



names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))



names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))



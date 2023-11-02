import math


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_matrix()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)

        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            for position in range(PhotoAlbum.PHOTOS_PER_PAGE):
                if self.photos[page][position] is None:
                    self.photos[page][position] = label
                    return f"{label} photo added successfully on page {page + 1} slot {position + 1}"

        return "No more free slots"

    def display(self):
        pass

    def build_matrix(self):
        result = list()

        for _ in range(self.pages):
            result.append([None] * self.PHOTOS_PER_PAGE)

        return result

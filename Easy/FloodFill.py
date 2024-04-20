def fill(image, sr, sc, color, curl):

    if sr < 0 or sr >= len(image):
        return

    if sc < 0 or sc >= len(image):
        return

    if cur != image[sr][sc]: return

    image[sr][sc] = color

    fill(image, sr-1, sc, color, cur)
    fill(image, sr+1, sc, color, cur)
    fill(image, sr, sc-1, color, cur)
    fill(image, sr, sc+1, color, cur)


def floodFill(image, sr, sc, color):
    if image[sr][sc] == color: return image

    fill(image, sr, sc, color, image[sr][sc])
    return image

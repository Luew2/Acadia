import random

# Sticker Types
stickerTypes = ["funny giraffe cartoon", "harry potter cartoon", "great dane cartoon"]


# Select sticker type
def randomSticker() -> str:
    """Returns a random sticker type"""
    # Randomly select sticker type
    sticker = random.randrange(0, len(stickerTypes))
    print("Generating a " + stickerTypes[sticker])
    return stickerTypes[sticker]

import random

# Sticker Types
stickerTypes = ["funny giraffe sticker", "harry potter sticker", "great dane sticker"]

# Select sticker type
def randomSticker() -> str:
    '''Returns a random sticker type'''
    # Randomly select sticker type
    sticker = random.randrange(0, len(stickerTypes))
    print ("Generating a " + stickerTypes[sticker])
    return stickerTypes[sticker]
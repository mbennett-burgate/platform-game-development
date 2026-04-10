list2: List[number] = []

def on_a_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -100
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    pass
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)

mySprite: Sprite = None
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . . . . f f f f . . . . .
        . . f f f f f f f f . . .
        . f f f f f f c f f f . .
        f f f f f f c c f f f c .
        f f f c f f f f f f f c .
        c c c f f f e e f f c c .
        f f f f f e e f f c c f .
        f f f b f e e f b f f f .
        . f 4 1 f 4 4 f 1 4 f . .
        . f e 4 4 4 4 4 4 e f . .
        . f f f e e e e f f f . .
        f e f b 7 7 7 7 b f e f .
        e 4 f 7 7 7 7 7 7 f 4 e .
        e e f 6 6 6 6 6 6 f e e .
        . . . f f f f f f . . . .
        . . . f f . . f f . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level0
    """))
mySprite.ay = 200
scene.camera_follow_sprite(mySprite)
for value in list2:
    pass
# TheGauntlet
This is a TUI dungeon crawler


Below is the main game loop logic in PyGame

Events -> User events (key press, mouse move, etc.)
Loop -> Game loop that manipulates artifacts within the game that is not the user (NPC movement, score update, etc.)
Render -> Logic to Re-render what is on the screen

while True:
    events()
    loop()
    render()
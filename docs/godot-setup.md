# Godot Setup Reference

## Project Settings
- Rendering > Textures > Default Texture Filter: Nearest
- Display > Window > Stretch > Mode: canvas_items
- Display > Window > Stretch > Scale Mode: integer
- Display > Window > Viewport: 640x360
- Display > Window > Override: 1280x720
- Rendering > 2D > Snap 2D Transforms to Pixel: on

## Isometric Tile Settings
- TileSet Tile Shape: Isometric
- TileSet Tile Size: 64x32
- TileMapLayer Y Sort Enabled: on

## Art Pipeline
- Sprite tool: Aseprite
- Plugin: Aseprite Wizard (install via Godot AssetLib)
- All sprites export with Nearest filter

## Headless Commands
- Godot binary: `/Applications/Godot.app/Contents/MacOS/Godot`
- Import: `/Applications/Godot.app/Contents/MacOS/Godot --headless --path game/ --import`
- Run and quit: `/Applications/Godot.app/Contents/MacOS/Godot --headless --path game/ --quit`

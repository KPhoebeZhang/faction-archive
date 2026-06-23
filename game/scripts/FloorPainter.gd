extends Node2D

func _ready() -> void:
	var floor_layer := $Floor as TileMapLayer
	for x in range(-5, 5):
		for y in range(-5, 5):
			floor_layer.set_cell(Vector2i(x, y), 0, Vector2i(0, 0))

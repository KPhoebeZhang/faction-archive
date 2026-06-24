extends CharacterBody2D

const SPEED := 80.0
const INTERACT_RADIUS := 80.0

var _backend: Node

func _ready() -> void:
	position = Vector2(320, 180)
	_backend = get_node("/root/BackendManager")

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.keycode == KEY_E and event.pressed and not event.echo:
		_interact_nearest_npc()

func _interact_nearest_npc() -> void:
	var npcs := get_parent().get_node_or_null("NPCs")
	if not npcs:
		return
	var nearest: Node = null
	var nearest_dist := INTERACT_RADIUS
	for npc in npcs.get_children():
		var dist: float = position.distance_to(npc.position)
		if dist < nearest_dist:
			nearest_dist = dist
			nearest = npc
	if nearest:
		_backend.call_interact(nearest.npc_id, "linger")

func _physics_process(_delta: float) -> void:
	var dir := Vector2.ZERO
	if Input.is_action_pressed("ui_up") or Input.is_key_pressed(KEY_W):
		dir += Vector2(-1.0, -0.5)
	if Input.is_action_pressed("ui_down") or Input.is_key_pressed(KEY_S):
		dir += Vector2(1.0, 0.5)
	if Input.is_action_pressed("ui_left") or Input.is_key_pressed(KEY_A):
		dir += Vector2(-1.0, 0.5)
	if Input.is_action_pressed("ui_right") or Input.is_key_pressed(KEY_D):
		dir += Vector2(1.0, -0.5)
	if dir != Vector2.ZERO:
		dir = dir.normalized()
	velocity = dir * SPEED
	move_and_slide()

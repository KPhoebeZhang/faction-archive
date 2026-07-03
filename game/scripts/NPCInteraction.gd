extends Area2D

@export var npc_id: String = ""

var _dialogue_ui: Node
var _backend: Node

var _player_inside: bool = false
var _player_ref: Node2D = null
var _presence_timer: float = 0.0
var _linger_cooldown: float = 0.0
var _linger_count: int = 0

const LINGER_TIME: float = 4.0
const LINGER_COOLDOWN: float = 30.0

func _ready() -> void:
	_dialogue_ui = get_tree().get_root().find_child("UI", true, false)
	_backend = get_node("/root/BackendManager")
	_backend.interaction_complete.connect(_on_interaction_complete)
	body_entered.connect(_on_body_entered)
	body_exited.connect(_on_body_exited)

func _process(delta: float) -> void:
	if _linger_cooldown > 0.0:
		_linger_cooldown -= delta

	if not _player_inside:
		return

	_presence_timer += delta
	if _presence_timer >= LINGER_TIME and _linger_cooldown <= 0.0:
		_linger_count += 1
		_linger_cooldown = LINGER_COOLDOWN
		_presence_timer = 0.0
		print("Linger triggered for %s (count: %d)" % [npc_id, _linger_count])

		if _linger_count == 2:
			_trigger_back_rub()
		else:
			_backend.call_interact(npc_id, "linger")

func _trigger_back_rub() -> void:
	print("Back-rub gesture triggered")
	var color_rect := get_node("ColorRect")
	var offset := Vector2.ZERO
	if _player_ref != null:
		offset = (_player_ref.global_position - global_position).normalized() * 8.0
	var original_pos: Vector2 = color_rect.position
	var tween := create_tween()
	tween.tween_property(color_rect, "position", original_pos + offset, 0.5)
	tween.tween_property(color_rect, "position", original_pos, 0.5)
	_dialogue_ui.show_dialogue("Mother", "Her hand finds your back. Just for a moment.")

func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		print("Player entered range of %s" % npc_id)
		_player_inside = true
		_player_ref = body
		_presence_timer = 0.0
		_backend.call_interact(npc_id, "approach")

func _on_body_exited(body: Node2D) -> void:
	if body is CharacterBody2D:
		_player_inside = false
		_player_ref = null
		_presence_timer = 0.0

func _on_interaction_complete(npc_id: String, dialogue: String, trust: float, tier: int) -> void:
	if npc_id != self.npc_id:
		return
	print("Interaction complete: %s" % dialogue)
	_dialogue_ui.show_dialogue("Mother", dialogue)

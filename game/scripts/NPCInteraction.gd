extends Area2D

@export var npc_id: String = ""

var _dialogue_ui: Node
var _backend: Node

var _player_inside: bool = false
var _player_ref: Node2D = null
var _stillness_timer: float = 0.0
var _linger_cooldown: float = 0.0
var _stillness_origin: Vector2 = Vector2.ZERO

const LINGER_TIME: float = 4.0
const MOVE_THRESHOLD: float = 5.0
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

	if not _player_inside or _player_ref == null:
		return

	if _player_ref.global_position.distance_to(_stillness_origin) > MOVE_THRESHOLD:
		_stillness_timer = 0.0
		_stillness_origin = _player_ref.global_position
		return

	_stillness_timer += delta
	if _stillness_timer >= LINGER_TIME and _linger_cooldown <= 0.0:
		_backend.call_interact(npc_id, "linger")
		print("Linger triggered for %s" % npc_id)
		_linger_cooldown = LINGER_COOLDOWN
		_stillness_timer = 0.0

func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		print("Player entered range of %s" % npc_id)
		_player_inside = true
		_player_ref = body
		_stillness_timer = 0.0
		_stillness_origin = body.global_position
		_backend.call_interact(npc_id, "approach")

func _on_body_exited(body: Node2D) -> void:
	if body is CharacterBody2D:
		_player_inside = false
		_player_ref = null
		_stillness_timer = 0.0

func _on_interaction_complete(npc_id: String, dialogue: String, trust: float, tier: int) -> void:
	if npc_id != self.npc_id:
		return
	print("Interaction complete: %s" % dialogue)
	_dialogue_ui.show_dialogue("Mother", dialogue)

extends Area2D

@export var npc_id: String = ""

var _dialogue_ui: Node
var _backend: Node

func _ready() -> void:
	_dialogue_ui = get_tree().get_root().find_child("UI", true, false)
	_backend = get_node("/root/BackendManager")
	_backend.interaction_complete.connect(_on_interaction_complete)
	body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		print("Player entered range of %s" % npc_id)
		_backend.call_interact(npc_id, "approach")

func _on_interaction_complete(id: String, dialogue: String, _trust: int, _tier: String) -> void:
	if id != npc_id:
		return
	print("Interaction complete: %s" % dialogue)
	_dialogue_ui.show_dialogue("Mother", dialogue)

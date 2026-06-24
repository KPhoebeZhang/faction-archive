extends CanvasLayer

var _npc_name_label: Label
var _dialogue_line_label: Label

func _ready() -> void:
	visible = false

	var panel := PanelContainer.new()
	panel.position = Vector2(120, 260)
	panel.size = Vector2(400, 80)
	panel.custom_minimum_size = Vector2(400, 80)
	add_child(panel)

	var vbox := VBoxContainer.new()
	panel.add_child(vbox)

	_npc_name_label = Label.new()
	_npc_name_label.name = "NPCName"
	var bold_font := SystemFont.new()
	bold_font.font_weight = 700
	_npc_name_label.add_theme_font_override("font", bold_font)
	_npc_name_label.add_theme_font_size_override("font_size", 10)
	vbox.add_child(_npc_name_label)

	_dialogue_line_label = Label.new()
	_dialogue_line_label.name = "DialogueLine"
	_dialogue_line_label.add_theme_font_size_override("font_size", 10)
	_dialogue_line_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	vbox.add_child(_dialogue_line_label)

func show_dialogue(npc_name: String, line: String) -> void:
	_npc_name_label.text = npc_name
	_dialogue_line_label.text = line
	visible = true
	await get_tree().create_timer(4.0).timeout
	visible = false

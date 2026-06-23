extends CharacterBody2D

const SPEED := 80.0

func _physics_process(_delta: float) -> void:
	var dir := Vector2.ZERO
	if Input.is_action_pressed("ui_up"):
		dir += Vector2(-1.0, -0.5)
	if Input.is_action_pressed("ui_down"):
		dir += Vector2(1.0, 0.5)
	if Input.is_action_pressed("ui_left"):
		dir += Vector2(-1.0, 0.5)
	if Input.is_action_pressed("ui_right"):
		dir += Vector2(1.0, -0.5)
	if dir != Vector2.ZERO:
		dir = dir.normalized()
	velocity = dir * SPEED
	move_and_slide()

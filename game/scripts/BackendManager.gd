extends Node

signal interaction_complete(npc_id: String, dialogue: String, trust: int, tier: String)

const BASE_URL = "http://localhost:8000"


func _ready() -> void:
	check_health()


func call_interact(npc_id: String, interaction_type: String) -> void:
	var http := HTTPRequest.new()
	add_child(http)
	http.request_completed.connect(_on_interact_response.bind(http, npc_id))
	var body := JSON.stringify({"npc_id": npc_id, "interaction_type": interaction_type})
	http.request(BASE_URL + "/interact", ["Content-Type: application/json"], HTTPClient.METHOD_POST, body)


func _on_interact_response(result: int, _code: int, _headers: PackedStringArray, body: PackedByteArray, http: HTTPRequest, npc_id: String) -> void:
	http.queue_free()
	if result != HTTPRequest.RESULT_SUCCESS:
		push_error("BackendManager: /interact request failed (result %d)" % result)
		return
	var json := JSON.new()
	if json.parse(body.get_string_from_utf8()) != OK:
		push_error("BackendManager: failed to parse /interact response")
		return
	var data: Dictionary = json.get_data()
	interaction_complete.emit(npc_id, data.get("dialogue", ""), data.get("trust", 0), data.get("tier", ""))


func check_health() -> void:
	var http := HTTPRequest.new()
	add_child(http)
	http.request_completed.connect(_on_health_response.bind(http))
	http.request(BASE_URL + "/health")


func _on_health_response(result: int, _code: int, _headers: PackedStringArray, body: PackedByteArray, http: HTTPRequest) -> void:
	http.queue_free()
	if result != HTTPRequest.RESULT_SUCCESS:
		push_error("BackendManager: /health request failed (result %d)" % result)
		return
	print("BackendManager health: ", body.get_string_from_utf8())

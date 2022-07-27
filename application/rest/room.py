import json

from flask import Blueprint, Response, request

from rentomatic.repository.memrepo import MemRepo
from rentomatic.requests.room_list import build_room_list_request
from rentomatic.responses import ResponseTypes
from rentomatic.use_cases.room_list import room_list_use_case
from rentomatic.serializers.room import RoomJsonEncoder

blueprint = Blueprint("room", __name__)

rooms = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "size": 405,
        "price": 66,
        "longitude": 0.18228006,
        "latitude": 51.74640997,
    },
    {
        "code": "913694c6-435a-4366-ba0d-da5334a611b2",
        "size": 56,
        "price": 60,
        "longitude": 0.27891577,
        "latitude": 51.45994069,
    },
    {
        "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
        "size": 93,
        "price": 48,
        "longitude": 0.33894476,
        "latitude": 51.39916678,
    },
]

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}


@blueprint.route("/rooms", methods=["GET"])
def room_list():
    query_parameters = {"filters": {}}

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            query_parameters["filters"][arg.replace("filter_", "")] = values

    request_object = build_room_list_request(filters=query_parameters["filters"])

    repo = MemRepo(rooms)
    result = room_list_use_case(repo, request_object)

    if result:
        return Response(
            json.dumps(result.value, cls=RoomJsonEncoder),
            mimetype="application/json",
            status=200,
        )
    else:
        return Response(
            json.dumps(result.value),
            mimetype="application/json",
            status=STATUS_CODES[result.response_type],
        )

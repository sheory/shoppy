from flask import Blueprint
from flask import jsonify
from flask import request

import json

from app.modules.product import create, update, get_product_by_id

product_blueprint = Blueprint("product", __name__)

@product_blueprint.route('/new/save', methods=['POST'])
@product_blueprint.route('/<int:id>/save', methods=['POST', 'PUT'])
def save(id: int = None):
    """Create or update a product.

    Args:
        id (int, optional): Product ID.

    Returns:
        Response: 200 for update
        Response: 201 for insertion
        Response: 400 for payload error

    """
    data = json.loads(request.get_data())
    if id:
        try:
            product = update(id, data)
            status_code = 200
        except NotImplementedError:
            return (
                jsonify({
                    "msg": "Impossible to update a deleted product"
                }), 403
            )
    else:
        try:
            product = create(data)
            status_code = 201
        except Exception as e:
            status_code = 400
            print(str(e))

    return jsonify({"msg": "ok", "product_id": product.id}), status_code


@product_blueprint.route('/<int:id>/info')
def get_info(id):
    """Get the information of a specific product

    Args:
        id (int): Product ID

    Returns:
        Response: 200, dict

    """

    try:
        product = get_product_by_id(id)
        response =  jsonify({"data": product}), 200
    except:
        response = jsonify({"msg": "Product not found"}), 404

    return response

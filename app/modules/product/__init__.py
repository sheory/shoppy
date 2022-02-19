from app.modules.product.model import Product

from typing import Dict
from typing import List
from typing import Tuple

from  app.model import get_db
db = get_db()

def create(data: Dict) -> "Product":
    """Create a new Product

    Args (dict): Product data

    Returns:
        Product: Instance of the created product

    """
    product = Product(**data)

    db.session.add(product)
    db.session.commit()

    return product


def update(id: int, data: dict) -> "Product":
    """Update a Product

    Args:
        id (int): Product ID
        data (dict): Product data

    Raises:
        NotImplementedError: For updating a deleted product

    Returns:
        Product: Instance of the updated Product

    """
    product = Product.query.get(id)

    if product._deleted:
        raise NotImplementedError

    product.update(**data)
    db.session.commit()

    return product

def get_product_by_id(id: int) -> "Product":
    """Get a product based on it id

    Args:
        id (int): product ID

    Raises:
        AttributeError: For product with the specified id not found

    Returns:
        Product: Product Instance

    """

    try:
        product = Product.query.get(id)
    except:
        raise AttributeError

    data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "status": product.status,
        "_deleted": product._deleted
    }

    return data

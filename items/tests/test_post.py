import django.test as dt

import flip_cart.constants.inputs.users as fciu
import flip_cart.constants.inputs.items as fcii
import flip_cart.constants.responses.items as fcri
import flip_cart.constants.urls as fcu
import flip_cart.tests.assert_equal_responses as fta
import items.models as im
import users.models as um


class Test(dt.TestCase):
    def test_post(self):
        users_input = fciu.post(1)
        self.client.post(fcu.USERS, users_input)
        self.client.post(fcu.AUTHS, users_input)

        items_input = fcii.post(1)
        response = self.client.post(fcu.ITEMS, items_input)

        fta.assert_equal_responses(response, fcri.ITEM_CREATED)
        user = um.User.objects.get(pk=1)
        item = im.Item.objects.get(pk=1)
        assert item.name == items_input["name"]
        assert item.description == items_input["description"]
        assert item.price == items_input["price"]
        assert item.mrp == items_input["mrp"]
        assert item.seller == user

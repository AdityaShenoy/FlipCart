import django.test as dt

import flip_cart.constants.inputs.users as fciu
import flip_cart.constants.inputs.items as fcii
import flip_cart.constants.responses as fcr
import flip_cart.constants.urls as fcu
import flip_cart.tests.assert_equal_responses as fta
import flip_cart.tests.get_response_data as ftg


class Test(dt.TestCase):
    def test_get(self):
        users_input = fciu.post(1)
        self.client.post(fcu.USERS, users_input)
        self.client.post(fcu.AUTHS, users_input)

        item_input = fcii.post(1)
        self.client.post(fcu.ITEMS, item_input)

        response = self.client.get(fcu.items_id(1))

        fta.assert_equal_responses(response, fcr.SUCCESS)

        response_data = ftg.get_response_data(response)["item"]
        assert all(response_data[k] == item_input[k] for k in item_input)
        assert response_data["seller"] == 1
        assert response_data["id"] == 1

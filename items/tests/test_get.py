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

        items_input_1 = fcii.post(1)
        self.client.post(fcu.ITEMS, items_input_1)
        items_input_2 = fcii.post(2)
        self.client.post(fcu.ITEMS, items_input_2)

        response = self.client.get(fcu.ITEMS)

        fta.assert_equal_responses(response, fcr.SUCCESS)

        response_data = ftg.get_response_data(response)["items"]
        assert all(
            response_data[0][k] == items_input_1[k]  # ___________
            for k in items_input_1
        )
        assert all(
            response_data[1][k] == items_input_2[k]  # ___________
            for k in items_input_2
        )

        assert response_data[0]["seller"] == 1
        assert response_data[1]["seller"] == 1

        assert response_data[0]["id"] == 1
        assert response_data[1]["id"] == 2

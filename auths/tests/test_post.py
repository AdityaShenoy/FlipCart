import django.test as dt

import flip_cart.constants.inputs.users as fciu
import flip_cart.constants.responses.auths as fcra
import flip_cart.constants.urls as fcu
import flip_cart.tests.assert_equal_responses as fta
import users.models as um


class Test(dt.TestCase):
    def test_post(self):
        input_ = fciu.post(1)
        um.User.objects.create_user(**input_)
        response = self.client.post(fcu.AUTHS, input_)
        fta.assert_equal_responses(response, fcra.AUTH_SUCCESS)
        assert self.client.session["_auth_user_id"] == "1"

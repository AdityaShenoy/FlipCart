import django.test as dt

import flip_cart.constants.inputs.users as fciu
import flip_cart.constants.responses.users as fcru
import flip_cart.constants.urls as fcu
import flip_cart.tests.assert_equal_responses as fta
import users.models as um


class Test(dt.TestCase):
    def test_post(self):
        input_ = fciu.post(1)
        response = self.client.post(fcu.USERS, input_)
        fta.assert_equal_responses(response, fcru.USER_CREATED)
        user = um.User.objects.get(pk=1)
        user.username = input_["username"]
        user.email = input_["email"]
        user.first_name = input_["first_name"]
        user.last_name = input_["last_name"]
        user.check_password(input_["password"])

import pytest
from src.randomizers import randomizer_person, randomizer_company, randomizer_digit
from src.api import user_id
from src.helper import asserts

"""Проверка создания записи пользователя"""


def test_create_user():
    first_name_er = randomizer_person.generate_first_name_female()
    user = user_id.post(user_id=randomizer_digit.generate_int_digit(period_from=0, period_to=100),
                        first_name=first_name_er,
                        last_name=randomizer_person.generate_last_name_female(),
                        patronymic=randomizer_person.generate_middle_name_female(),
                        age=randomizer_digit.generate_int_digit(period_from=0, period_to=100),
                        position=randomizer_company.generate_profession_name(),
                        company=randomizer_company.generate_company_name(),)

    asserts.status_code(response=user)
    first_name = user.json().get("first_name", 'There is no key first_name')
    asserts.equal(actual_result=first_name, expected_result=first_name_er, message="AR ! ER")

    id_ = user.json().get("id", 'There is no key id')

    show_user_data = user_id.get(id_=id_)
    first_name_check_post = show_user_data.json().get("first_name", 'There is no key first_name')

    asserts.equal(actual_result=first_name_check_post, expected_result=first_name_er, message="AR ! ER")

    first_name_patch_er = randomizer_person.generate_first_name_male()
    update_user_data = user_id.patch(user_id=id_,
                                     first_name=first_name_patch_er,
                                     last_name=randomizer_person.generate_last_name_male(),
                                     patronymic=randomizer_person.generate_middle_name_male(),
                                     age=randomizer_digit.generate_int_digit(period_from=1, period_to=99),
                                     position=randomizer_company.generate_profession_name(),
                                     company=randomizer_company.generate_company_name())

    #
    asserts.status_code(response=update_user_data)
    first_name_patch = update_user_data.json().get("first_name", 'There is no key first_name')
    asserts.equal(actual_result=first_name_patch, expected_result=first_name_patch_er, message="AR ! ER")

    delete_user_data = user_id.delete(id_=id_)
    asserts.status_code(response=delete_user_data)





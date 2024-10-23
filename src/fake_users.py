from src.randomizers import randomizer_person
from src.randomizers import randomizer_digit
from src.randomizers import randomizer_company

fake_users = [
    {"id": randomizer_digit.generate_int_digit(period_from=0, period_to=10),
     "first_name": randomizer_person.generate_first_name_male(),
     "last_name": randomizer_person.generate_last_name_male(),
     "patronymic": randomizer_person.generate_middle_name_male(),
     "age": randomizer_digit.generate_int_digit(period_from=1, period_to=99),
     "position": randomizer_company.generate_profession_name(),
     "company": randomizer_company.generate_company_name()}
    for _ in range(5)

]

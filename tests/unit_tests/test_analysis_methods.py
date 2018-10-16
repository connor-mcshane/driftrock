import src.models as models
import src.calc_methods as calc


def test_most_sold_item():
    """
    Barebones test for calculating the most sold item, tests the following cases:
    """

    users = _build_user_list(2)
    item1_purchases = _build_purchase_list(users, 20, "light-saber")
    item2_purchases = _build_purchase_list(users, 10, "crossbow")
    all_purchases = item1_purchases + item2_purchases

    assert calc.most_sold_item(all_purchases) == ["light-saber"]
    
    #
    item1_purchases_less = _build_purchase_list(users, 10, "light-saber")
    # use sets so the list order isn't important
    assert set(calc.most_sold_item(item1_purchases_less + item2_purchases)) == set(["light-saber", "crossbow"])


def test_total_spend_for_user():
    """[summary]


    """

    # make a list of users
    users = _build_user_list(10)

    # each user buys 10 items at one dollar each
    purchases = _build_purchase_list(users, 10, "light-saber")

    for user in users:
        assert calc.total_spend_for_user(user.email, purchases, users) == 10


def test_most_loyal_customer():


    users = _build_user_list(2)
    loyal_customer = users[0]

    item1_purchases = _build_purchase_list(users, 10, "light-saber")
    item2_purchases = _build_purchase_list([loyal_customer], 10, "crossbow")
    all_purchases = item1_purchases + item2_purchases
    assert calc.most_loyal_customer(all_purchases, users) == [loyal_customer.email] 


def _build_user_list(number_users):

    user_list = []
    for i in range(number_users):
        user_name = "id_" + str(i)
        email = "drift" + str(i) + "rock@email.com"
        user_list.append(models.User(user_name, email))

    return user_list

def _build_purchase_list(user_list, purchase_per_user, purchase_item):
    purchase_list = []
    for user in user_list:
        for i in range(purchase_per_user):
            purchase_list.append(models.Purchase(user.id, purchase_item, "1.0"))

    return purchase_list
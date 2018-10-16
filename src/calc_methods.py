from collections import defaultdict


def most_sold_item(purchase_list):
    """
    Return a list of items (str) with the most number of sales. We return a list in case
    muiltiple items have the same number of sales
    """

    item_sales = defaultdict(
        lambda: 0)  # default number of purchase_list are 0
    max_count = 0
    for purchase in purchase_list:
        item = purchase.item
        item_sales[item] += 1
        max_count = max(max_count, item_sales[item])

    return _keys_from_matching_value(item_sales, max_count)


def total_spend_for_user(email, purchase_list, user_list):
    """
    Given an email (str) and list of Purchase objects and list of User objects
    return a value for the total spend
    """

    user_id = _user_id_from_email(email, user_list)

    if user_id is None:
        raise ValueError("User email {} does not exist!".format(email))

    total_spend = 0
    for purchase in purchase_list:
        if user_id == purchase.user_id:
            total_spend += float(purchase.spend)

    return total_spend


def most_loyal_customer(purchase_list, user_list):
    """
    Given a list of Purchase objects and list of User objects
    return a value for the total spend
    """

    purchase_list_per_user = defaultdict(
        lambda: 0)  # default number of purchase_list are 0
    max_count = 0
    for purchase in purchase_list:
        user_id = purchase.user_id
        purchase_list_per_user[user_id] += 1
        max_count = max(max_count, purchase_list_per_user[user_id])

    # grab id with the biggest amounts
    user_ids = _keys_from_matching_value(purchase_list_per_user, max_count)

    return _emails_from_user_list(user_ids, user_list)


# Helper methods


def _user_id_from_email(email, user_list):
    for user in user_list:
        if email == user.email:
            return user.id


def _emails_from_user_list(user_ids, user_list):
    emails = []

    # Two loops, as we may need to find muiltiple emails for muiltple users
    for user_id in user_ids:
        for user in user_list:
            if user_id == user.id:
                emails.append(user.email)
                break  # to outer loop

    return emails


def _keys_from_matching_value(input_dict, comp_val):
    return [key for key, val in input_dict.items() if comp_val == val]

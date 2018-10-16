import argparse
import src.driftrock_api as ap
import src.calc_methods as calc
import re
import sys


def main():
    """ Main function used to switch between features """

    command, parameter = _arg_parser(sys.argv[1:])

    if command not in ["most_sold", "total_spend", "most_loyal"]:
        print("Invalid command passed!")
        return

    api = ap.DriftRockAPI()
    if api.resource_status_not_ok():
        print("Resource is not okay, please try again later")
        return

    if command == "most_sold":
        result = _most_sold(api)

    elif command == "total_spend":
        result = _total_spend(api, parameter)

    elif command == "most_loyal":
        result = _most_loyal(api)
    
    else:
        result = ""

    return result 


def _arg_parser(args):
    description = """ Run the script to find either the:\n  
                    1. Most sold item  e.g >> python app most_sold \n
                    2. Total spend for a user e.g >> python app total_spend me@mail.com \n
                    3. Most loyal user e.g >> python app most_loyal """

    command_help = """ Command must be either 'most_sold', 'total_spend' or
                        'most_loyal' """

    parameter_help = " Email address of the user "

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("command", type=str, help=command_help)
    parser.add_argument("parameter", type=str, nargs='?', help=parameter_help)
    args = parser.parse_args(args)

    return args.command, args.parameter


# Helper functions


def _most_sold(api_handler):
    purchases = api_handler.get_all_purchases()
    most_sold = calc.most_sold_item(purchases)
    _print_list(most_sold)
    return most_sold


def _total_spend(api_handler, email):
    # check the email before we query the API
    if email is None or _invalid_email_format(email):
        print("Invalid email format!")
        return

    purchases = api_handler.get_all_purchases()
    user_list = api_handler.get_all_users()
    total_spend = calc.total_spend_for_user(email, purchases, user_list)
    print(total_spend)
    return total_spend


def _most_loyal(api_handler):
    purchases = api_handler.get_all_purchases()
    user_list = api_handler.get_all_users()

    loyal_customer = calc.most_loyal_customer(purchases, user_list)
    _print_list(loyal_customer)
    return loyal_customer


def _invalid_email_format(email):
    regex = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
    match = re.match(regex, email)

    return match is None


def _print_list(list_to_print):
    for entry in list_to_print:
        print(entry)


if __name__ == "__main__":
    main()

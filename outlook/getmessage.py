import pyOutlook

def outlook_get_messages(access_token):

    try:
        account = pyOutlook.OutlookAccount(access_token)

        inbox_messages = account.get_messages()

        sent_messages = account.sent_messages()

        return {'status': 'Pass', 'inbox_messages': inbox_messages, 'sent_messages': sent_messages, 'error': None}

    except pyOutlook.internal.errors.AuthError as error:
        return {'status': 'Fail', 'error': 'Authentication failed'}

    except pyOutlook.internal.errors.APIError as error:
        return {'status': 'Fail', 'error': 'API error occurred'}

    except Exception as error:
        return {'status': 'Fail', 'error': str(error)}


access_token = "EwBYA+l3BAAUFFpUAo7J3Ve0bjLBWZWCclRC3EoAAbJu5QadRR6K5t33OIQlbSz0dvLj+AwlNjv5m2MuXns9mCYxlru53fO3nO1/SJ+mfIE93bpfS6FYMt5TZtCcb7y8inYS1Ra9pM8ouwITjMvFaITIXT71zDqA5O9cMJhbUpFaaXAcRN65Am7Lu7U3+G2dLw4HQo4XIox1o3952P6iwiaUxavIHVFDETRst7UXOn/XwlxCBIqglKOIu5mi3sbHMrUowRWvCSYeTk3Ba8XicrZ3W4KFYou1y6BvMtGEwS44p+bWCVsznoIlQ3Dt3iT3XwmnAiSvfrSkFsV5Ta6I8x3PCYEUaAGT9TVASz5owxYf/W9IPywTM2BLE4lNF08DZgAACHkKkMQI/Vs+KAIoPGDOJWqUWciKgt0UOp2GUApdL2RhZ3qBzfijjrSGfiZBV9s/D7lPtRXYPLWZxzIX+w5qnuqGqICsxYbubwNiihmxayTSfnDeEf9CPYG8zG3Eu/M3wZddt2H4iLsRgb95g45+XJLGzImLXwiOtRGrPo2okTSIFM8xBTYd/+3Qo6GH6Gn4PBTQoaydMEwXzbWGwHRxe+Lp+WrfaX/MlCD/kzMR/oYx/ORP31I89dYVIbE7Ximq5f4n94X/KkbM0Y4QNJz4KlNy670WSC1ZBFjV8vbvW1RUM5fA/yTqR4H2yjc/RUuA1ilhXGM8lG3NWxhYKBmI4mFJYmIBYB0GlMNQ8kqZY+KUEpW46bslcJ95vXlDZprCajR96TpwRPXFq/n0SQOUZrIbLNLuvqr85trnlOo27xol1CzXft/3r8KU0Emm6IAaI3R7oqrxIJv/8Hz2sWB930YSRQj3M4HXVx/S5XlCrD5cfhksJJF7X8p66Yb1Uyh3QAmY2hKHb1i8DtZKCQ6N9vNxfq8vlRv9R9oeDKwFCzozKv/bmgTP5wyso+2EovJYee5VjSXVo84CNvBZZXKo0TgGZPKipa9NTHJ0u6V1oSsBVS3Jcnao8Xaja1C4mSJCHU+60INwb+tLFgBbFHHq8/9FCFd6jUzi2awl+5zV5XqdIcU0NpDoiaAJzz6p7WafvtfnRVNkb1npOnMcb/BDFLBvRfDDRHovR2JLWF206k3q039jAg=="
result = outlook_get_messages(access_token)

print(result)

import pyOutlook

def outlook_get_folders(access_token):

    try:
        account = pyOutlook.OutlookAccount(access_token)

        all_folders = account.get_folders()

        return {'status': 'Pass', 'folders': all_folders, 'error': None}

    except pyOutlook.internal.errors.AuthError as error:
        return {'status': 'Fail', 'error': 'Authentication failed'}

    except pyOutlook.internal.errors.APIError as error:
        return {'status': 'Fail', 'error': 'API error occurred'}

    except Exception as error:
        return {'status': 'Fail', 'error': str(error)}


access_token='EwBYA+l3BAAUFFpUAo7J3Ve0bjLBWZWCclRC3EoAAdCUgN4EOoD3gHxibrl9yCigb/zH6PMk5tN3lSM7ImHMHbIUgVzVGCdN1d3sOKa4Y7dWhfH5lipiqm0gq29e2hj61F7micaPkQO42L9VP7f/4MUjxKCzLv5YSpddXwkTtfQ/uD1BCW5w1G1B/CqNZXvy4Lh7UU218sLpZeXGC6gsGS1Cl6uQcqPSlaKWkoCTtclqJAbZoqgAL4LcDUVtvL1w77Yx2MfOVViwFa5KVtxh4X+M/6llwp24LQ9Uf7l9gA+d7JbfS+79aq4dKZVXNP1dKXI/9d0yJA2hIEsCdBLAufVWmRR4sJ1hSohH032rBmVL874Z7RD4OAvds4bnqSwDZgAACKJUgAIUtHvrKAI01O44STXiJ/xKYR1ZKame8VaYc6VTmBynf1cxXCoTe7b45Q0yhJNDtuZv9BXwGJULhA/VOc6GhHYmwSKFhGW0SUbzNT1etYHmTlCfqDJFD1GfZasd0o+Gp1N1kU970dA1edIl2/oaj/FpzXA7rfV/jRsqGLJG9Wjjd9GP2cSoJHbqj3RZXC1WeopSueloGsspenyO+Aar9PAb/IZ4ZSqW29gOjWxUbFsAV+xhOB0C13iTQB3QHAzquWRyH8hmyKnX1WfFeTA5eYZRAiZHnfLnKfrpZYiJeTb/ab+AV0EXUtz+Ort7wBJMSu4ZQOcgf6l8D2dRguuXvSTWiqKWAPCcTJHYhaPXkaLtCeam97ETY9Sb9gbDSl/WaXIlFnauv3c4HBtXgt7ps08xs4D93COrpXNt4nrFWrG3Gy72eSII0r8JGPRR2KtYB0fEsEhx7ar9smnOqmo86lwTsXwzfcflNmEd2XKuinV4Z89FiqvAL2vTatKgP5IXY5v1pZTYgz/tzKHatcgNQYse2unlCJcmpLBrYqTfG5VH6Ph18g5BOjVrbsi7Avj7TnEvzR0PPczocYJfuhNYr2GhJCJh8oHEW4TMdbyBc9Cufq++mZeVin1wo8VTYkw78H8n79RSrIGyeRpb2rwmNlWFSj2caca/JrEwxhQbd8PkkGkuAAoEbWHmZrntXI96yuoQK7g2Wcacw5FFAG5RKCqS7U1EDklAu59TYKz1JKJjAg=='

result = outlook_get_folders(access_token)

print(result)

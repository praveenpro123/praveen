from pyOutlook import OutlookAccount, Contact, internal
import time


def outlook_send_mail(access_token, mail_subject, mail_body, mail_to):

    try:
        account = OutlookAccount(access_token)

        email = account.new_email(mail_body, mail_subject, [Contact(mail_to)])

        email.send()

        time.sleep(5)

        message_uid = 0

        messages = account.get_messages()

        for i in range(0, len(messages)):

            if str(messages[i]) == mail_subject:

                message_uid = messages[i].message_id

                print('message id : '+ message_uid)

                break

        return {'status': 'Pass', 'message_id': str(message_uid), 'error': None}

    except internal.errors.AuthError as error:

        return {'status': 'Fail', 'error': 'Authentication failed'}

    except internal.errors.APIError as error:

        return {'status': 'Fail', 'error': 'API error occured'}

    except Exception as error:

        return {'status': 'Fail', 'error': str(error)}


access_token = 'EwBYA+l3BAAUFFpUAo7J3Ve0bjLBWZWCclRC3EoAARvBx8EsF9/iAcOs9CW4f3L4IpGgFro12N0qPpyp4Yk7IHEQQtkM6B6FnS3v0TEfdEh2P1eKSAqLf3NfJWB4FAMiHVQbEjwqxPhk5rCfzufisiXr+eqTMqMyAyMTYq1JnfVS2rCzc88GN6GcH2D8N06X7G23SbQUQY0+NIgRe/fB0LvcJu5uhg85VSTrTkcz/BZ1e4LHFewzFrAHnozJB3HKYBSlLU0CGlQ6Qd6rkTKZIfE10N8otTCNNNJBCZQ30sqEjVgcHLvkfm/QN8UGTwv2teehjHLUCfJ0tsQJzK6owk5HkkW+mYuMZdllL6XZ04Y6mTvrXJzxq8ZLAm5mE9cDZgAACAiNAHNKu5BeKAIXCvyz0m8eg3cQwTomWt36kq5R2ML7yCpVbf0exKDhjsotpQmrDPM5HlyQdGv6EvuTsmzL+y/4OGLFokAQ1rjQ39uziBNfU7qpFWXqKnK1jRHmgWlPeEu8++dSjkBGQkrXa1YFaiNewyh1pQsA0t/t8e9o8X3DcMtLVCyEgyVqjyLsBTd3vBKFu/CVivZNgtDCXEYsLzb9lnocQJ9qGluctQGCKAeM6QK55fiK/bwGaWnxmXr1Yf1iOuPiMnD6u0JxtPaY42lHYrhl+/6gB0RqLLZyTAOgPCYeacliwpA1eg+rSrjHQAFFizfjYHKrNAj00kddTxvGHaOLBIh7asXnUSCo6aOQYjI670vHepFP7QSPXa6jyWCfEGdteUR6Pa/5MBnOItfn4QYEugk/yXOr4ovp28V/DKXmW4JHglUnN5RevA45A7pdG+eCYmEV8jB0EX18xzgb5Fn06mSFiBLsu2iQnLi04LIo5IuoH5SK2ZABjtZgMnVWD8oDt7llPwqTmMzN74EwCfdwR4Fn7suBGyOf2urGB/i7+sFTTZ6v6kHbGPxefsI22MRqfm29yzVOTPLgWQ/Unf8SWRMw1tVSrC4bST9nRxkRhcZcAIQhWll59pAT9B7e84OWug8KunAkmui0v924IpZfv92ffq5qdNVuAYX4pyIGx2JrlHiva86kC7wvTsXB49xPoaCEl8ry43KdfnwlJT6SfQgWNjLtCSSDcx80r65jAg=='
mail_subject = 'Testing outlook codes'
mail_body = 'Hi,Please let me know if you are getting a message'
mail_to = 'pravin.hz@gmail.com'

result = outlook_send_mail(access_token, mail_subject, mail_body, mail_to)

print(result)

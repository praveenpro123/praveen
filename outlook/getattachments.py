import pyOutlook

def outlook_get_attachments(access_token, mail_subject, message_id_value):

    try:
        account = pyOutlook.OutlookAccount(access_token)

        email_subjects = account.get_messages()

        index = 0

        count = 0

        for i in range(0, len(email_subjects)):
        
            if str(email_subjects[i]) == str(mail_subject):

                if str(email_subjects[i].message_id) == str(message_id_value):

                    index = i

                    break

                else:
                    count = count + 1

            else:
                count = count + 1

        if count == len(email_subjects):

            return {'status': 'Fail', 'error': 'Email with the subject '+ mail_subject +' not found'}

        else:

            attachment = email_subjects[index].attachments

            return {'status': 'Pass', 'attachments': attachment, 'error': None}

    except pyOutlook.internal.errors.AuthError as error:
        return {'status': 'Fail', 'error': 'Authentication Failed'}

    except pyOutlook.internal.errors.APIError as error:
        return {'status': 'Fail', 'error': 'API error occurred'}

    except Exception as error:
        return {'status': 'Fail', 'error': str(error)}



access_token = 'EwBYA+l3BAAUFFpUAo7J3Ve0bjLBWZWCclRC3EoAARvBx8EsF9/iAcOs9CW4f3L4IpGgFro12N0qPpyp4Yk7IHEQQtkM6B6FnS3v0TEfdEh2P1eKSAqLf3NfJWB4FAMiHVQbEjwqxPhk5rCfzufisiXr+eqTMqMyAyMTYq1JnfVS2rCzc88GN6GcH2D8N06X7G23SbQUQY0+NIgRe/fB0LvcJu5uhg85VSTrTkcz/BZ1e4LHFewzFrAHnozJB3HKYBSlLU0CGlQ6Qd6rkTKZIfE10N8otTCNNNJBCZQ30sqEjVgcHLvkfm/QN8UGTwv2teehjHLUCfJ0tsQJzK6owk5HkkW+mYuMZdllL6XZ04Y6mTvrXJzxq8ZLAm5mE9cDZgAACAiNAHNKu5BeKAIXCvyz0m8eg3cQwTomWt36kq5R2ML7yCpVbf0exKDhjsotpQmrDPM5HlyQdGv6EvuTsmzL+y/4OGLFokAQ1rjQ39uziBNfU7qpFWXqKnK1jRHmgWlPeEu8++dSjkBGQkrXa1YFaiNewyh1pQsA0t/t8e9o8X3DcMtLVCyEgyVqjyLsBTd3vBKFu/CVivZNgtDCXEYsLzb9lnocQJ9qGluctQGCKAeM6QK55fiK/bwGaWnxmXr1Yf1iOuPiMnD6u0JxtPaY42lHYrhl+/6gB0RqLLZyTAOgPCYeacliwpA1eg+rSrjHQAFFizfjYHKrNAj00kddTxvGHaOLBIh7asXnUSCo6aOQYjI670vHepFP7QSPXa6jyWCfEGdteUR6Pa/5MBnOItfn4QYEugk/yXOr4ovp28V/DKXmW4JHglUnN5RevA45A7pdG+eCYmEV8jB0EX18xzgb5Fn06mSFiBLsu2iQnLi04LIo5IuoH5SK2ZABjtZgMnVWD8oDt7llPwqTmMzN74EwCfdwR4Fn7suBGyOf2urGB/i7+sFTTZ6v6kHbGPxefsI22MRqfm29yzVOTPLgWQ/Unf8SWRMw1tVSrC4bST9nRxkRhcZcAIQhWll59pAT9B7e84OWug8KunAkmui0v924IpZfv92ffq5qdNVuAYX4pyIGx2JrlHiva86kC7wvTsXB49xPoaCEl8ry43KdfnwlJT6SfQgWNjLtCSSDcx80r65jAg=='
mail_subject = 'Testing Remaining'
message_id_value = 'AQMkADAwATMwMAItYTBiMy1iYzc0LTAwAi0wMAoARgAAAwpkTC5OnHFLmUE-GNnP0cgHAFjVNSxktD9EjC2nUzdbESQAAAIBDAAAAFjVNSxktD9EjC2nUzdbESQABGkll9wAAAA='

result = outlook_get_attachments(access_token, mail_subject, message_id_value)
print(result)

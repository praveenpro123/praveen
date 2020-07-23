import pyOutlook

def outlook_move_mail(access_token, mail_subject, move_folder, message_id_value):

    try:
        account = pyOutlook.OutlookAccount(access_token)

        messages = account.get_messages()

        mail_index = 0

        mail_count = 0

        for i in range(0, len(messages)):

            if str(messages[i]) == mail_subject:

                if str(messages[i].message_id) == str(message_id_value):

                    mail_index = i

                    break

                else:
                    mail_count = mail_count + 1

            else:

                mail_count = mail_count + 1


        if mail_count == len(messages):

            return {'status': 'Fail', 'error': 'Email with the subject '+ mail_subject +' not found'}

        folders = account.get_folders()

        folder_index = 0

        folder_count = 0

        for i in range(0, len(folders)):

            if str(folders[i]) == move_folder:

                folder_index = i

                break

            else:

                folder_count = folder_count + 1

        if folder_count == len(folders):

            return {'status': 'Fail', 'error': 'Folder with the name '+ move_folder +' not found'}

        else:

            messages[mail_index].move_to(folders[folder_index])

            return {'status': 'Pass', 'error': None}
            
    except pyOutlook.internal.errors.AuthError as error:
        return {'status': 'Fail', 'error': 'Authentication Failed'}

    except pyOutlook.internal.errors.APIError as error:
        return {'status': 'Fail', 'error': 'API error occurred'}
        
    except Exception as error:
        return {'status': 'Fail', 'error': str(error)}



access_token = 'EwBYA+l3BAAUFFpUAo7J3Ve0bjLBWZWCclRC3EoAAdEVzZxmrhuHjHfvaO/D+m7WgYd6uKJwtYhMzS7Tzvlj6VKFYUFx0OPSGTuFTYaibTg0ZKBe45/k4ww58Kq623o8YZ4aYyvoS8ifIkiZSUEl11XBPuLKbjOcf7fC577kuunHtoFUSvGXsmigBeJwYTVVeyl8hAw6wRLB3CvA1cga+VJzJv6e30IVEtyq1gBEEl2OUb4BONO7DN9IBCKWW4vZXmEWO9UUlUG9ieaxPgFmmpS9uZTZ11NdrZKQj216DOMWydATPzEEh+qVM5ITZpvnOkY94fdoEcHyNL/MxeZxu2Wpmvxf5phYpFfkzyq4uG3Dk80kvEYdGDdBHVEXupwDZgAACO+BqRhpfON4KAITseroCaCoOTfY+7vtAiQSbT0q9yErx+js8RiCWXLZM61G0fLmXEOEy+b4ZlEhDvZ8kBQjkG1flnzuc6HAReVNkKsAcU8wgg8NPXiJatcOduxSRhsbDbeh7IncBleekKyZX+pSBkgDzCdr3EaZUwxSnuOBvcIafEtv4dUrMl6SlZSqFD9m6QKAIEAbsrQaMzJ9xdRHGvByhZ7Xkef8A03mqoqcXOq7waAqMbKdbpJNGNboHmFlbAdeMyZbzN5nRACPQCGP7jr/dW9bSwcArQ3a1T4lTRSIG0lHWCgvcjUA+v2OJDpktM/9y9S3wcsKAjwRH/ii0wa1Jo0zmjjhsOO3JTjJx1qf/cy3P4IfI1tFR/a31wOUP/hbiI4nyjzprcawL0OCPmcAks0zirwlQ30Ij0S3WNCG6XevpF9kWOoXuD0YMzZp5IOFEnxAbOpjAiyAVN+nGTqkKRhF5y4ruy35b8zPIXV9sxIus7dMIsuB2i2SpvHXBWoL6r5i9befSFPRIQTEnxFzcqKpy49vd/usiMv1fLkxpXD3CbMWnceTlIXAEZSk0/mAHc7VGBsZzPYzgmSSGWN38fdaEQoqasrw1IPBv6P6+nh7nuGlxU2ELMDFwBXqg4mrG/evxAcnsyZnO60NbGO0XiuWSshQy3J1cW/WP7YSISH8GAU/spkZbGKV3Z6dyOZdZjrteGtgU5A4lnslduXaMNw+fdnSNribGOxh7NvALgBjAg=='
mail_subject = 'India'
move_folder = 'Drafts'
message_id_value = 'AQMkADAwATMwMAItYTBiMy1iYzc0LTAwAi0wMAoARgAAAwpkTC5OnHFLmUE-GNnP0cgHAFjVNSxktD9EjC2nUzdbESQAAAIBIQAAAFjVNSxktD9EjC2nUzdbESQABGgkfuoAAAA='

result = outlook_move_mail(access_token, mail_subject, move_folder, message_id_value)

print(result)



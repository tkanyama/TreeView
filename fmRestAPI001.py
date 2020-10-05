import fmrest
fms = fmrest.Server('https://192.168.0.171',
                        user='admin',
                        password='',
                        database='FMServer_Sample',
                        layout='タスク',verify_ssl=False)
fms.login()
record = fms.get_record(1)
record.name
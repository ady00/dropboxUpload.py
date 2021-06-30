import dropbox

# for some reason, I never turned this assignment in even though I had finished it about 2-3 months ago. I believe you shared/helped me write this code as we went over it in class. 


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)







def main():
    access_token = 'sl.AgbyIoY7fgh7YLOMrnYKuYuUiYiP9PSkiEnmJmHgHzkLJ8mukl_zSQjT8oLVfn_AkB4Yn6O0ghj67GhjVHRPoLFEVvwg3_p2A67fnKjhghj78vbnV0SKhk6nbU2-tYhTAB' # eneter in the access code given to you in your app
    transferData = TransferData(access_token)






    file_from = input("Enter filename to transfer")
    file_to = input("Enter the file name to upload(full path name)")




    transferData.upload_file(file_from, file_to)
    print("Good job! FIle has been moved")


main()

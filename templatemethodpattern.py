class BaseRecord:

    def save(self):        
        try:
            self.beforeSave()
            # Save to DB
            self.saveSucceded()
        except:
            self.saveFailed()
        finally:
            self.afterSave()

    def beforeSave(self):
        raise NotImplemented

    def afterSave(self):
        raise NotImplemented

    def saveFailed(self):
        raise NotImplemented

    def saveSucceded(self):
        raise NotImplemented


class User(BaseRecord):

    def beforeSave(self):
        print('Trying to save user...')

    def afterSave(self):
        print('Clear the logs...')

    def saveFailed(self):
        print('Saving of user failed...')

    def saveSucceded(self):
        print('Saving of user succeded...')



class Post(BaseRecord):

    def beforeSave(self):        
        print('Trying to save post...')
        raise Exception()

    def afterSave(self):
        print('Clear the logs...')

    def saveFailed(self):
        print('Saving of post failed...')

    def saveSucceded(self):
        print('Saving of post succeded...')


def main():

    user = User()
    post = Post()

    user.save()
    post.save()

main()
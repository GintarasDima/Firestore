class FirestoreClient:
    def __init__(self):
        self.config = {
            #key to Firebase
        }
        self.db_client = self.get_client(self.config)



    @staticmethod
    def get_client(config):
        cred = credentials.Certificate(config)
        firebase_admin.initialize_app(cred, {'projectId': 'intership-a3a41'})
        return firestore.client()

    def get_document(self, collection_id, document_id):
        return self.db_client.collection(collection_id).document(document_id).get().to_dict()

    def set_document(self, collection_id, document_id, data):
        return self.db_client.collection(collection_id).document(document_id).set(data)


firestore_client = FirestoreClient()
firestore_client.set_document('collection1', 'document2', {'1': 1970, '2': [1, 6, 0, 1]})
document = firestore_client.get_document('collection1', 'document2')
print(document)
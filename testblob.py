from azure.storage.blob import BlockBlobService
account="tswchallenge2"
sas="?sv=2016-05-31&ss=b&srt=sco&sp=rwdlac&se=2017-07-11T14:31:16Z&st=2017-07-11T06:31:16Z&spr=https&sig=IYysT%2BZYwOmFWSSxAuUrVSd%2FjvAZ%2BcpcITTvOy5X3sM%3D"
block_blob_service = BlockBlobService(account_name=account, sas_token=sas)
block_blob_service.create_blob_from_text('videos','pythontest.txt','test blob')
